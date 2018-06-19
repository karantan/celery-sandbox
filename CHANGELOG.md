Changelog
=========


0.1.0 (unreleased)
------------------

- Add celery_sandbox basic file structure. Also add first sandbox example
  (retries.py).

- Add `retries_exceeded_v2` that shows how MaxRetriesExceededError can be
  handeled without try/except - by using `if`.

- Add `retries_exceeded_return` that shows that we can also use `return`
  instead of `retry` as long as we do not pass `throw=False` to retry method.
