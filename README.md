# Celery Sandbox

Sandbox for testing celery stuff

## Installation

You need to have [`pipenv` installed](https://docs.pipenv.org/#install-pipenv-today).
Then run:
```bash
$ pipenv install
```

Because we are testing celery things you will also need to install
[redis](https://redis.io/). 

On OSX you can do:

```
$ brew install redis
```

And then you need to start it:

```
$ brew services start redis
```

Now you are ready to start playing with sandbox scripts. Have fun and I hope you
learn something.


### How to `retries.py`

First run the celery worker:

```
$ pipenv run celery worker -A celery_sandbox.retries -l info
```

Then open ipython in a new terminal, import `retries_exceeded` function and run it.

```
$ pipenv run ipython
...
In [1]: from celery_sandbox.retries import retries_exceeded
In [2]: retries_exceeded.delay(1, 2)
```

Results will be seen in the first terminal.


#### Testing

Before you run the tests make sure redis is running. Then run:

```
$ pipenv run pytest celery_sandbox
```


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request