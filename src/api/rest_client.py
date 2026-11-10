import requests
from src.config.settings import settings

class RestClient:
    def __init__(self, base_url: str = settings.api_base_url, timeout: int = settings.api_timeout):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def get(self, path: str, **kwargs):
        return self.session.get(
            f"{self.base_url}/{path.lstrip('/')}",
            timeout=self.timeout,
            **kwargs,
        )

    def post(self, path: str, payload: dict, **kwargs):
        return self.session.post(
            f"{self.base_url}/{path.lstrip('/')}",
            json=payload,
            timeout=self.timeout,
            **kwargs,
        )
