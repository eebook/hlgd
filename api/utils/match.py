#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "knarfeh@outlook.com"
import re
import logging
from ..url_metadata.models import Metadata

LOGGER = logging.getLogger(__name__)


def _get_regex_dict():
    metadata_list = Metadata.query.all()
    site_regex_dict = {item.name: item.regex for item in metadata_list}
    return site_regex_dict


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
