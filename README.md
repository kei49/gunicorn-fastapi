# gunicorn-fastapi

## How to run fastapi on gunicorn workerss

```
poetry shell
poetry install
gunicorn main:app
curl http://localhost:8080
```

## How it works?

- run_only_once function of main.py will run only once due to preload_app=True inside gunicorn.conf.py
- basic logs by gunicorn will be stored inside gunicorn-logs.log
- when calling the app multiple times, you will see mutliple workers work by seeing the worker pid

## Refernce

- [FastAPI: Server Workers - Gunicorn with Uvicorn](https://docs.gunicorn.org/en/latest/index.html)
- [Gunicorn - WSGI server](https://docs.gunicorn.org/en/latest/index.html)
