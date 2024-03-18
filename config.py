import os

from dotenv import load_dotenv

load_dotenv()


class PaymeConfig:
    BASE_URL: str = os.getenv("PAYME_BASE_URL")
    PAYCOM_ID: str = os.getenv("PAYCOM_ID")
    CALLBACK_URL: str = os.getenv("PAYME_CALLBACK_URL")


class UzumConfig:
    BASE_URL: str = os.getenv("UZUM_BASE_URL")
    TOKEN: str = os.getenv("UZUM_TOKEN")
    CALLBACK_URL: str = os.getenv("UZUM_CALLBACK_URL")
