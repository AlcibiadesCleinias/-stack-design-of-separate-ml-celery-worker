from celery.execute import send_task
from celery.result import AsyncResult


# TODO: ABC should be relocated...
class MlModelNameAppClientABC:
    """Abstraction to leave possibility to use RESTfull API or to use Celery and Celery broker, etc."""
    def __init__(self, *args, **kwargs):
        pass

    def post_predict(self, *args,  **kwargs) -> str:
        """Start predicting, get id."""
        pass

    def get_progress(self, task) -> int:
        """Get progress by task id."""
        pass

    def get_predict(self, task: str):
        """Get predict result task by id."""
        pass


class MlModelNameAppCeleryClient(MlModelNameAppClientABC):
    # should be synced with app settings
    def __init__(self, *args, **kwargs):
        # TODO: from settings
        self.task_name = 'MlModelName'
        self.task_queue = 'queueForPolls'

    def post_predict(self, *args,  **kwargs) -> str:
        print('post predict..')
        task = send_task(self.task_name, args=args, kwargs=kwargs, queue=self.task_queue)
        return task

    def get_predict(self, task):
        """Get predict result by id."""
        return AsyncResult(task).get()

    # TODO: other methods
