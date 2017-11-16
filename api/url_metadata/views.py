#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import uuid
from flask import request

from ..common.utils import json
from ..common.exceptions import FieldValidateFailed
from ..common import status
from . import url_metadata_bp

LOGGER = logging.getLogger(__name__)


@url_metadata_bp.route('', methods=["POST"])
@json
def get_url_metadata():
    data = request.json
    LOGGER.info('data???{}'.format(data))
    return {}


