#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "knarfeh@outlook.com"
import re


# TODO: get this from each repo
SITE_REGEX_DICT = {
    'rss': [
        'atom'
    ],
    'talkpython': '(?<=talkpython\.fm/episodes/)(?P<subject_id>[^/\n\r]*)(/)',
    'zhihu': [
        '(?<=zhihu\.com/)people/(?P<author_id>[^/\n\r]*)'
    ]
}



def get_website_type(url):
    for k, v in SITE_REGEX_DICT.items():
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
