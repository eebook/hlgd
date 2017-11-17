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
from .models import Metadata

LOGGER = logging.getLogger(__name__)


@url_metadata_bp.route('', methods=["POST"])
@json
def get_url_metadata():
    data = request.json
    LOGGER.info('data???{}'.format(data))
    url_type = get_website_type(data['url'])
    return {}

@url_metadata_bp.route('/sync', methods=["PUT"])
@json
def sync_metadata():
    metadata_objs = Metadata.query.filter().all()
    LOGGER.info("metadata???{}".format(metadata_objs))
    # if catalog folder not exist, git clone
    catalog_path = Path('/catalog')
    if not catalog_path.exists():
        clone_repo('/catalog', current_app.config['CATALOG_URL'])
    update_repo('/catalog')
    return {}
