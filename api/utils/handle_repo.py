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
    for root, dirs, files in os.walk('/catalog/json', followlinks=False):
        print(root)
        print(dirs)
        print(files)
        # for item in files
        # result.append(os.path.join(root, files))
        file_path_list = ['/catalog/json/'+item for item in files]
    for item in file_path_list:
        result_item = _get_json(item)
        result.append(result_item)
    return result
