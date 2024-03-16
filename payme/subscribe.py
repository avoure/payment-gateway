from dataclasses import dataclass

import requests


@dataclass
class SubscribeAPI:
    """
    Implements Payme Subscribe API methonds
    Documentation: https://developer.help.paycom.uz/metody-subscribe-api/
    """

    base_url: str
    paycom_id: str

    def _api_call(self, payload: dict | None = None) -> dict:
        if payload is None:
            return {}
        headers: dict = {"X-Auth": self.paycom_id}
        payme_method: str = payload["method"]
        full_url: str = f"{self.base_url}/{payme_method}"

        response: requests.Response = requests.post(url=full_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

    def cards_create(self, number: str, expire: str, save: bool = True) -> dict:
        """https://developer.help.paycom.uz/metody-subscribe-api/cards.create"""

        payload: dict = {
            "method": "cards.create",
            "params": {
                "card": {
                    "number": number,
                    "expire": expire,
                },
                "save": save,
            },
        }
        return self._api_call(payload)

    def cards_get_verify_code(self, token: str) -> dict:
        """https://developer.help.paycom.uz/metody-subscribe-api/cards.get_verify_code"""

        payload: dict = {
            "method": "cards.get_verify_code",
            "params": {
                "token": token,
            },
        }
        return self._api_call(payload)

    def cards_verify(self, verify_code: int, token: str) -> dict:
        """https://developer.help.paycom.uz/metody-subscribe-api/cards.verify"""

        payload: dict = {"method": "cards.verify", "params": {"token": token, "code": verify_code}}
        return self._api_call(payload)

    def cards_check(self, token: str) -> dict:
        """https://developer.help.paycom.uz/metody-subscribe-api/cards.check"""

        payload: dict = {
            "method": "cards.check",
            "params": {
                "token": token,
            },
        }

        return self._api_call(payload)

    def cards_remove(self, token: str) -> dict:
        """https://developer.help.paycom.uz/metody-subscribe-api/cards.remove"""

        payload: dict = {
            "method": "cards.remove",
            "params": {
                "token": token,
            },
        }
        return self._api_call(payload)
