#!/bin/sh
python manage.py db upgrade

crontab /src/etc/crontab.list
echo "crontab list:"
crontab -l

supervisord --nodaemon -c /src/etc/supervisord.conf

