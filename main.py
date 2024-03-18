from fastapi import FastAPI

from payme.api import payme_router
from uzum.api import uzum_router

app = FastAPI()

app.include_router(payme_router, tags=["Payme"], prefix="/api/v1/payme")
app.include_router(uzum_router, tags=["Uzum"], prefix="/api/v1/uzum")


@app.get("/api/healthcheck")
def root():
    return {"message": "alive"}
