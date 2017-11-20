#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from api.common.utils import get_log_config


class Config(object):
    LOG_HANDLER = os.getenv('LOG_HANDLER', 'debug,info,error').split(',')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
    LOG_PATH = os.getenv('LOG_PATH', '/var/log/eebook/')
    LOGCONFIG = get_log_config(component='hlgd', handlers=LOG_HANDLER, level=LOG_LEVEL, path=LOG_PATH)
    LOGCONFIG_QUEUE = ['eebook']

    DB_USER = os.getenv("DB_USER", 'postgres')
    DB_PASSWORD = os.getenv("DB_PASSWORD", None)
    DB_NAME = os.getenv("DB_NAME", "postgres")
    DB_HOST = os.getenv("DB_HOST", "db")
    DB_PORT = os.getenv("DB_PORT", 5432)
    DB_ENGINE = os.getenv("DB_ENGINE", "postgresql")
    SQLALCHEMY_DATABASE_URI = '{db_engine}://{user_name}:{password}@{hostname}/{database}'.\
                              format_map({
                                  'db_engine': DB_ENGINE,
                                  'user_name': DB_USER,
                                  'password': DB_PASSWORD,
                                  'hostname': DB_HOST,
                                  'database': DB_NAME
                              })
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PAGINATE_BY = os.getenv('PAGINATE_BY', 10)
    CATALOG_URL = 'https://github.com/eebook/catalog'

    HLGD_HEADERS = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'HLGD/v1.0'
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    LOG_HANDLER = os.getenv('LOG_HANDLER', 'debug,info,error').split(',')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_PATH = os.getenv('LOG_PATH', '/var/log/eebook/')
    LOGCONFIG = get_log_config(component='hlvs', handlers=LOG_HANDLER, level=LOG_LEVEL, path=LOG_PATH)


config = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig,
}
