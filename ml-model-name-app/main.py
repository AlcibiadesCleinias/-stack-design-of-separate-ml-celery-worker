from config.celery import app
from ml.model_name import ModelName


@app.task(name='MlModelName')
def ml_model_name_predict(*args, **kwargs):
    print('start predicting')
    ModelName().predict(args, kwargs)
    return 10001
