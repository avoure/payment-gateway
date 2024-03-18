from fastapi import APIRouter

from . import models
from .nasiya import NasiyaAPI

uzum_router = APIRouter()

_nasiya_api = NasiyaAPI()


@uzum_router.post("/nasiya/check-status")
async def check_buyer_status(payload: models.CheckStatus):
    return _nasiya_api.check_status(payload)
