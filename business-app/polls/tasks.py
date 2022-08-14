from config.celery import app


@app.task(name='MlModelName')
def _raise_task(*args, **kwargs):
    raise Exception("never should be called by design")
