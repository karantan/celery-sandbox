from celery_sandbox.retries import retries_exceeded
from celery_sandbox.retries import retries_exceeded_v2
from celery_sandbox.retries import retries_exceeded_return


def test_retries_exceeded(celery_app, celery_worker):
    assert retries_exceeded.delay(3, 4).get() == 'Max retries exceeded...'


def test_retries_not_exceeded(celery_app, celery_worker):
    assert retries_exceeded.delay(4, 4).get() == 8


def test_retries_v2_exceeded(celery_app, celery_worker):
    assert retries_exceeded_v2.delay(3, 4).get() == 'Max retries exceeded...'


def test_retries_v2_not_exceeded(celery_app, celery_worker):
    assert retries_exceeded_v2.delay(4, 4).get() == 8


def test_retries_exceeded_return(celery_app, celery_worker):
    assert retries_exceeded_return.delay(3, 4).get() == 'Max retries exceeded...'


def test_retries_not_exceeded_return(celery_app, celery_worker):
    assert retries_exceeded_return.delay(4, 4).get() == 8
