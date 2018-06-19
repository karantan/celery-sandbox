from celery import Celery
from celery.exceptions import MaxRetriesExceededError


class CeleryConfig(object):
    BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


app = Celery(config_source=CeleryConfig)


@app.task(bind=True)
def retries_exceeded(self, x, y):
    if x == y:
        return x + y
    try:
        raise Exception('puf ...')
    except Exception as err:
        try:
            # If you add `exc=err` the "Exception: puf ..." will be raised
            # instead of MaxRetriesExceededError.
            # raise self.retry(exc=err, countdown=1)
            raise self.retry(countdown=1)
        except MaxRetriesExceededError:
            return 'Max retries exceeded...'


@app.task(bind=True)
def retries_exceeded_v2(self, x, y):
    if x == y:
        return x + y
    try:
        raise Exception('puf ...')
    except Exception as err:
        if self.request.retries >= self.max_retries:
            return 'Max retries exceeded...'
        raise self.retry(exc=err, countdown=1)
