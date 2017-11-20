#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals


import logging

from .models import Metadata
from ..common.database import db
from .exceptions import MetadataException

LOGGER = logging.getLogger(__name__)


def insert_or_update(metadata):
    try:
        metadata_obj = Metadata(**metadata)
        insert_or_update_obj = db.session.merge(metadata_obj)
        db.session.add(insert_or_update_obj)
        db.session.commit()
    except Exception as e:
        LOGGER.error('Insert or update metadata, got error, traceback: %s', e)
        raise MetadataException(code='unknown_issue')
    return
