#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import uuid
from pathlib import Path
from flask import request, current_app

from ..common.utils import json
from ..common.exceptions import FieldValidateFailed
from ..common import status
from . import url_metadata_bp
from ..utils.match import get_website_type
from ..utils.handle_git import clone_repo, update_repo
from ..utils.handle_repo import get_metadata_from_repo
from .models import Metadata
from .infra import insert_or_update
from .exceptions import MetadataException

LOGGER = logging.getLogger(__name__)


@url_metadata_bp.route('', methods=["POST"])
@json
def get_url_metadata():
    data = request.json
    url_type = get_website_type(data['url'])
    metadata = Metadata.query.filter_by(name=url_type).first()
    if metadata is not None:
        result = {
            'name': metadata.name,
            'schema': metadata.schema,
            'repo': metadata.repo,
            'info': metadata.info,
            'image': metadata.image,
            'image_version': metadata.image_version
        }
        return result
    else:
        raise MetadataException('url_not_support')


@url_metadata_bp.route('/sync', methods=["PUT"])
@json
def sync_metadata():
    catalog_path = Path('/catalog')
    if not catalog_path.exists():
        clone_repo('/catalog', current_app.config['CATALOG_URL'])
    else:
        update_repo('/catalog')
    metadata_list = get_metadata_from_repo()
    for item in metadata_list:
        insert_or_update(item)
    return {}
