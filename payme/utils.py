import base64

from config import PaymeConfig

from .models import GeneratePayLink


def generate_pay_link(info: GeneratePayLink) -> str:
    """
    return link example:
    """
    payload: str = f"m={info.payme_id};ac.{info.payme_account}={info.order_id};a={info.amount};c={info.callback_url}"
    encoded_payload = base64.b64encode(payload.encode("utf-8"))

    return f"{PaymeConfig.BASE_URL}/{str(encoded_payload, 'utf-8')}"
