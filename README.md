# Stack Design with Separate ML Celery Worker
In this repo there is a draft view on how we could divide ML (on python) and api/business logic (Django, Celery Beat) 
with help of Celery and Redis as a task broker and tmp result storing.

# Purpose & Predicaments
I want ML to be as a separate microservice with its own requirements and etc., with logic to make predict only 
(no logic about how to save results, where to save, etc - I call it as a business part). 
I could not put ML into a simple RESTfull API coz of a nature of complexity of ML and ML task time-consuming. I could not
put task into [business-app/polls/tasks.py](business-app/polls/tasks.py) coz I will face with increased code & module 
complexity inside [business-app](business-app) itself.

# Solution Flow
In a few words: [business-app](business-app) -> Celery(via Redis) -> [ml-model-name-app](ml-model-name-app) -> Celery(via Redis) -> [business-app](business-app) -> Client.
Where [business-app](business-app) triggered by a Client -> API request or even by Celery Beat (Scheduler) task: in both cases - a business request.

More concrete and with code linking:
1. Business request from client of API (Django) or from a scheduler (Celery Beat based on Django) comes. 
And this request consists of request to make some ML predict.
2. Via [business-app/clients/ml_model_name_app.py](business-app/clients/ml_model_name_app.py) abstraction class task 
created and might be tracked.
3. [ml-model-name-app](ml-model-name-app) as a worker subscribed on a Celery queue in Redis and after executing saves result into redis
4. When it is needed [business-app](business-app) get result via [special ML-client class](https://github.com/AlcibiadesCleinias/stack-design-with-separate-ml-celery-worker/blob/main/business-app/clients/ml_model_name_app.py#L19) (i.e. from Redis) and either return to user via API or save into SQL DB, 
non-SQL DB with its logic

# Note
- [business-app](business-app) is a simple Django with polls app
- [business-app](business-app) uses abstraction to work with sending predict task. Thus, when ml app rewritten on e.g. API
you merely change methods of abstraction
- [ml-model-name-app/main.py](ml-model-name-app/main.py) writen in a view, route manner but uses Celery task registering under a hood 

# Start
```bash
docker-compose up
```

Start predict via api e.g. `http://localhost:8000/start-ml/`

Check foo predict via e.g. `http://localhost:8000/result-ml/` + your task id from previous url
