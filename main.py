from fastapi import FastAPI

from payme.api import payme_router

app = FastAPI()

app.include_router(payme_router, tags=["Payme"], prefix="/api/v1/payme")


@app.get("/api/healthcheck")
def root():
    return {"message": "alive"}
