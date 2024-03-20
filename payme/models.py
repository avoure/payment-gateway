from dataclasses import dataclass


@dataclass
class GeneratePayLink:
    payme_id: int
    payme_account: str
    order_id: str
    amount: int
    callback_url: str


@dataclass
class CardsCreate:
    number: str
    expire: str
    save: bool = True


@dataclass
class CardsGetVerifyCode:
    token: str


@dataclass
class CardsVerify:
    verify_code: int
    token: str


@dataclass
class CardsCheck:
    token: str


@dataclass
class CardsRemove:
    token: str
