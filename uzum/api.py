from fastapi import APIRouter

from . import models
from .nasiya import NasiyaAPI

uzum_router = APIRouter()

_nasiya_api = NasiyaAPI()


@uzum_router.post("/nasiya/check-status")
async def check_buyer_status(payload: models.CheckStatus):
    return _nasiya_api.check_status(payload)


@uzum_router.post("/nasiya/create-order")
async def check_buyer_status(payload: models.CreateOrder):
    """
    'create-order' could possibly be renamed to 'create-contract'
    """
    return _nasiya_api.create_order(payload)


@uzum_router.post("/nasiya/confirm-contract")
async def confirm_contract(payload: models.ConfirmContract):
    return _nasiya_api.confirm_contract(payload)
