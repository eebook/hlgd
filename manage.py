#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import os
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from api.common.database import db
from api import create_app

CURRENT_CONFIG_ENV = os.getenv('CURRENT_CONFIG_ENV', 'dev')

app = create_app(config_name=CURRENT_CONFIG_ENV)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(host="0.0.0.0", port=80))


if __name__ == "__main__":
    manager.run(default_command="runserver")
