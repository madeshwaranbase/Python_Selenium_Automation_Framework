from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

def _as_bool(value: str, default: bool = True) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"} if value else default

@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv(
        "BASE_URL",
        "https://rahulshettyacademy.com/seleniumPractise/#/",
    )
    browser: str = os.getenv("BROWSER", "chrome").lower()
    headless: bool = _as_bool(os.getenv("HEADLESS", "true"))
    wait_timeout: int = int(os.getenv("WAIT_TIMEOUT", "10"))
    api_base_url: str = os.getenv(
        "API_BASE_URL", "https://jsonplaceholder.typicode.com"
    ).rstrip("/")
    api_timeout: int = int(os.getenv("API_TIMEOUT", "15"))

settings = Settings()
