#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import logging
from werkzeug.exceptions import HTTPException, default_exceptions
from flask import Flask, Blueprint, request, jsonify
from flask_logconfig import LogConfig

from config import config
from .common.exceptions import APIException
from .common.middleware import response
from .common.utils import RegexConverter
from .common.database import db
from .common.diagnose import diagnose

BP_NAME = 'root'
root_bp = Blueprint(BP_NAME, __name__)
LOGGER = logging.getLogger(__name__)


@root_bp.route("/_ping", methods=["GET"])
def ping():
    return {"hlgd:": "pong"}

@root_bp.route("/_diagnose", methods=["GET"])
def diagnose_api():
    return diagnose()

def create_app(config_name='dev'):
    app = Flask(__name__)

    # IN
    @app.before_request
    def ensure_content_type():
        content_type = request.headers.get('Content-type')
        if not content_type == 'application/json':
            raise APIException('invalid_content_type')
    # OUT
    app.response_class = response.JSONResponse
    response.json_error_handler(app=app)
    # Load default configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    logcfg = LogConfig(app)
    logcfg.init_app(app)
    db.init_app(app)

    # Support regular expression
    app.url_map.converters['regex'] = RegexConverter
    app.register_blueprint(root_bp, url_prefix='/v1')

    from .url_metadata import url_metadata_bp
    app.register_blueprint(url_metadata_bp, url_prefix='/v1/url_metadata')

    return app
