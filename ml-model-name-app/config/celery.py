from celery import Celery

# TODO: from settings <- env
app = Celery(
    "config",
    broker="redis://redis:6379",
    backend="redis://redis:6379",
)
app.conf.task_routes = {
    'main.ml_model_name_predict': {'queue': 'queueForPolls'},
}
