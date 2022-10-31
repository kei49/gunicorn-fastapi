import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health_check():
    print(f"{os.getpid()} worker is handling the request")
    return {"message": "Hello World"}


def run_only_once() -> None:
    print("run_only_once: this runs only once when starting the app even with multiple workers of gunicron")
    
run_only_once()