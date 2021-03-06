#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import os
import logging
import json

LOGGER = logging.getLogger(__name__)

def _get_json(path):
    """
    Read a json file and return its content(Python object)
    :param path: json file path
    """
    with open(path, 'r') as f:
        return json.load(f)


def get_metadata_from_repo():
    result = list()
    for _, dirs, files in os.walk('/catalog/stable', followlinks=False):
        LOGGER.info("files: {}".format(files))
        # for item in files
        # result.append(os.path.join(root, files))
        file_path_list = ['/catalog/stable/'+item for item in files]
    for item in file_path_list:
        result_item = _get_json(item)
        result.append(result_item)
    return result
