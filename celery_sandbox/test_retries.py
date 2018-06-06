from celery_sandbox.retries import retries_exceeded


def test_retries_exceeded(celery_app, celery_worker):
    assert retries_exceeded.delay(3, 4).get() == 'Max retries exceeded...'


def test_retries_not_exceeded(celery_app, celery_worker):
    assert retries_exceeded.delay(4, 4).get() == 8
