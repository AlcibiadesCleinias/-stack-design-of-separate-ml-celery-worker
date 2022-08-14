from django.http import HttpResponse

from clients.ml_model_name_app import MlModelNameAppCeleryClient

m = MlModelNameAppCeleryClient()


# only for demonstration and testing
def start_ml(request):
    task = m.post_predict(1,2 ,4)
    html = f"<html><body>Ml started {task}</body></html>"
    return HttpResponse(html)


def result_ml(request, task):
    predict = m.get_predict(task)
    html = f"<html><body>{predict}</body></html>"
    return HttpResponse(html)
