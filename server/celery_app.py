import os
import sys

from celery import Celery

# make celery_config module available here
sys.path.append(os.path.join(os.getcwd(), "server"))
import celery_config  # noqa

# Todo: Add LOGGER from celery.utils.log for custom logging

celery_app = Celery("fast_api_base")
celery_app.config_from_object(celery_config, force=True)
celery_app.autodiscover_tasks(packages=["server.core.asynchronous"])
