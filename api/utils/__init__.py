#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import os
import logging
import json
import re

from ..url_metadata.models import Metadata
LOGGER = logging.getLogger(__name__)


def _get_json(path):
    """
    Read a json file and return its content(Python object)
    :param path: json file path
    """
    with open(path, 'r') as f:
        return json.load(f)


def _get_regex_dict():
    metadata_list = Metadata.query.all()
    site_regex_dict = {item.name: item.regex for item in metadata_list}
    return site_regex_dict


def _get_examples_dict():
    metadata_list = Metadata.query.all()
    site_examples_dict = {item.name: item.examples for item in metadata_list}
    return site_examples_dict


def get_template_content(file_path):
    with open(file_path) as f:
        content = f.read()
        f.close()
        return content


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


def get_website_type(url):
    # TODO: add cache
    site_regex_dict = _get_regex_dict()
    for k, v in site_regex_dict.items():
        if isinstance(v, str):
            search_result = re.search(v, url)
            if search_result is not None:
                return k
        elif isinstance(v, list):
            for item in v:
                search_result = re.search(item, url)
                if search_result is not None:
                  return k
    return 'unknown'


def get_website_examples():
    site_examples_dict = _get_examples_dict()
    return site_examples_dict
