bind = "localhost:8080"
reload = True
preload_app = True
proc_name = "fastapi_on_gunicorn"
loglevel = 'debug'
errorlog = 'gunicorn-logs.log'
worker_class = "uvicorn.workers.UvicornWorker"
workers = 4