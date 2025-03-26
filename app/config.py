import secrets
from zoneinfo import ZoneInfo

UTC = ZoneInfo("UTC")
WIB = ZoneInfo("Asia/Jakarta")

SECRET_KEY = secrets.token_hex(32)