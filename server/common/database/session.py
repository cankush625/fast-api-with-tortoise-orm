from tortoise.contrib.fastapi import register_tortoise

from server.config.settings import settings


def create_database_connection(app):
    register_tortoise(app=app, config=settings.TORTOISE_CONFIG)
