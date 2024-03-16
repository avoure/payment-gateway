import os

from dotenv import load_dotenv

load_dotenv()


class PaymeConfig:
    BASE_URL: str = os.getenv("PAYME_BASE_URL")
    PAYCOM_ID: str = os.getenv("PAYCOM_ID")
