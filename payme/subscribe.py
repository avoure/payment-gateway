from dataclasses import dataclass

import requests

from config import PaymeConfig

from . import models


@dataclass
class SubscribeAPI:
    """
    Implements Payme Subscribe API methonds
    Documentation: https://developer.help.paycom.uz/metody-subscribe-api/
    """

    def _api_call(self, payload: dict | None = None) -> dict:
        if payload is None:
            return {}

        base_url = PaymeConfig.BASE_URL
        paycom_id = PaymeConfig.PAYCOM_ID

        headers: dict = {"X-Auth": paycom_id}
        payme_method: str = payload["method"]
        full_url: str = f"{base_url}/{payme_method}"

        response: requests.Response = requests.post(url=full_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

    def cards_create(self, info: models.CardsCreate) -> dict:
        """https://developer.help.paycom.uz/metody-subscribe-api/cards.create"""

        payload: dict = {
            "method": "cards.create",
            "params": {
                "card": {
                    "number": info.number,
                    "expire": info.expire,
                },
                "save": info.save,
            },
        }
        return self._api_call(payload)

    def cards_get_verify_code(self, info: models.CardsGetVerifyCode) -> dict:
        """https://developer.help.paycom.uz/metody-subscribe-api/cards.get_verify_code"""

        payload: dict = {"method": "cards.get_verify_code", "params": {"token": info.token}}
        return self._api_call(payload)

    def cards_verify(self, info: models.CardsVerify) -> dict:
        """https://developer.help.paycom.uz/metody-subscribe-api/cards.verify"""

        payload: dict = {"method": "cards.verify", "params": {"token": info.token, "code": info.verify_code}}
        return self._api_call(payload)

    def cards_check(self, info: models.CardsCheck) -> dict:
        """https://developer.help.paycom.uz/metody-subscribe-api/cards.check"""

        payload: dict = {
            "method": "cards.check",
            "params": {
                "token": info.token,
            },
        }

        return self._api_call(payload)

    def cards_remove(self, info: models.CardsRemove) -> dict:
        """https://developer.help.paycom.uz/metody-subscribe-api/cards.remove"""

        payload: dict = {
            "method": "cards.remove",
            "params": {
                "token": info.token,
            },
        }
        return self._api_call(payload)
