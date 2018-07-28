#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Boolean, Integer, BigInteger
from sqlalchemy.dialects.postgresql import JSON

from ..common.database import BaseModel
from ..common.serializer import ModelSerializerMixin


class Metadata(BaseModel, ModelSerializerMixin):
    __tablename__ = "metadata"
    name = Column(String(36), primary_key=True)
    author = Column(String(128))
    author_link = Column(String(255))
    repo = Column(String(128))
    repo_type = Column(String(36), default="github")
    info = Column(String(255))
    schema = Column(JSON)
    examples = Column(JSON)
    regex = Column(String(255))
    image = Column(String(255))
    image_version = Column(String(255))

    def __repr__(self):
        return '<Metadata:%s>' % self.name

    def __str__(self):
        return self.__repr__()
