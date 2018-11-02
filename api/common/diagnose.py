#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import time
import os
import requests

from ..url_metadata.models import Metadata

LOGGER = logging.getLogger(__name__)
status_ok = 'OK'
status_error = 'ERROR'

def _current():
    return int(time.time()*1000)

def _get_db_info():
    start = _current()
    detail = {'status': 'OK'}
    try:
        Metadata.query.count()
    except Exception:
        detail['status'] = status_error
        detail['message'] = 'Query in db failed'
    detail['latency'] = str(_current() - start) + 'ms'
    return detail

def _get_github_info():
    start = _current()
    detail = {'status': status_ok}
    resp = requests.get('https://status.github.com/messages', timeout=5)
    if resp.status_code != 200:
        detail['status'] = status_error
    detail['latency'] = str(_current() - start) + 'ms'
    return detail

def diagnose():
    result = {'status': status_ok, 'details': []}
    checks = {
        'database': _get_db_info,
        'github': _get_github_info
    }
    for name, func in checks.items():
        detail = {'name': name, 'status': status_ok}
        try:
            detail.update(func())
            if detail['status'] == status_error:
                result['status'] = status_error
        except Exception as e:
            result['status'] = status_error
            detail['status'] = status_error
            detail['message'] = e.message
        result['details'].append(detail)
    return result

