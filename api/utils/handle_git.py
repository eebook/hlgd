#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import logging
from git import Repo

LOGGER = logging.getLogger(__name__)


def clone_repo(path, url, branch='master'):
    LOGGER.info('Clone repo: %s', url)
    Repo.clone_from(url, path)


def update_repo(path, branch='master'):
    LOGGER.info('Update repo')
    repo = Repo(path)
    origin = repo.remotes.origin
    origin.pull()


if __name__ == "__main__":
    clone_repo('/catalog', 'https://github.com/eebook/catalog')
    update_repo('/catalog')
