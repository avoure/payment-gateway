from fastapi import APIRouter

from config import PaymeConfig

from . import models
from .subscribe import SubscribeAPI
from .utils import generate_pay_link

payme_router = APIRouter()

_subscribe_api = SubscribeAPI(base_url=PaymeConfig.BASE_URL, paycom_id=PaymeConfig.PAYCOM_ID)


@payme_router.post("/subscribe/cards-create")
async def cards_create(payload: models.CardsCreate):
    return _subscribe_api.cards_create(payload)


@payme_router.post("/subscribe/cards-get-verify-code")
async def cards_get_verify_code(payload: models.CardsGetVerifyCode):
    return _subscribe_api.cards_get_verify_code(payload)


@payme_router.post("/subscribe/cards-verify")
async def cards_verify(payload: models.CardsVerify):
    return _subscribe_api.cards_verify(payload)


@payme_router.post("/subscribe/cards-check")
async def cards_check(payload: models.CardsCheck):
    return _subscribe_api.cards_check(payload)


@payme_router.post("/subscribe/cards-remove")
async def cards_remove(payload: models.CardsRemove):
    return _subscribe_api.cards_remove(payload)


@payme_router.post("/generate-pay-link")
async def generate_pay_link(payload: models.GeneratePayLink):
    return generate_pay_link(payload)
