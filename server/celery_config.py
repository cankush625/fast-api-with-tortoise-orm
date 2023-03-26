from kombu import Exchange, Queue

from config.settings import settings
from server.common.constants import CeleryQueue

broker_url = settings.CELERY_BROKER_URL
result_backend = settings.CELERY_BROKER_URL
accept_content = ["json"]
task_ignore_result = False
task_serializer = "json"
result_serializer = "json"
timezone = settings.TIME_ZONE
task_soft_time_limit = settings.CELERYD_SOFT_TIME_LIMIT
task_time_limit = settings.CELERYD_TIME_LIMIT

task_default_queue = CeleryQueue.DEFAULT_KEY
task_default_exchange = CeleryQueue.DEFAULT_KEY
task_default_routing_key = CeleryQueue.DEFAULT_KEY

task_queues = (
    Queue(
        CeleryQueue.DEFAULT_KEY,
        Exchange(CeleryQueue.DEFAULT_KEY),
        routing_key=CeleryQueue.DEFAULT_KEY,
    ),
    # Add custom queues when required
)
