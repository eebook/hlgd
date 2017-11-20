#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "knarfeh@outlook.com"
import re
import logging
from ..url_metadata.models import Metadata

LOGGER = logging.getLogger(__name__)


# For debug
SITE_REGEX_DICT = {
    'rss': [
        'atom'
    ],
    'talkpython': '(?<=talkpython\.fm/episodes/)(?P<subject_id>[^/\n\r]*)(/)',
    'zhihu': [
        '(?<=zhihu\.com/)people/(?P<author_id>[^/\n\r]*)'
    ]
}

def _get_regex():
    metadata_list = Metadata.query.all()
    site_regex_dict = {item.name: item.regex for item in metadata_list}
    return site_regex_dict


def get_website_type(url):
    # TODO: add cache
    site_regex_dict = _get_regex()
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


if __name__ == "__main__":
    website_type1 = get_website_type('https://talkpython.fm/episodes/asdf/')
    print('website type: {}'.format(website_type1))

    website_type2 = get_website_type('https://zhihu.com/people/knarfeh')
    print('website type: {}'.format(website_type2))
