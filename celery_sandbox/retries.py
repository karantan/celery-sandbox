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
            raise self.retry(throw=False, countdown=1)
        except MaxRetriesExceededError:
            return 'Max retries exceeded...'
