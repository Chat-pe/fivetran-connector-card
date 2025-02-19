from pprint import pprint
import base64
from collections.abc import Callable
from typing import Generic, Literal, Optional, TypeVar
from pydantic import BaseModel
from .env.py import API_KEY, SECRET
import requests

BASE_URL = "https://api.fivetran.com/v1"


encode_base64: Callable[[str], str] = lambda x: base64.b64encode(
    x.encode("ascii")
).decode("ascii")

T = TypeVar("T", bound=BaseModel)


def make_request(
    method: Literal["get", "post", "put", "patch", "delete"],
    endpoint: str,
    response_type: type[T],
    params: Optional[dict] = None,
    data: Optional[dict] = None,
    headers: Optional[dict] = None,
):
    url = f"{BASE_URL}{endpoint}"
    headers = headers or {}

    headers["Authorization"] = f"Basic {encode_base64(f'{API_KEY}:{SECRET}')}"

    print(f"{method.upper()}: {url}")
    pprint(params)
    pprint(data)
    response = requests.request(method, url, params=params, json=data,  headers=headers)
    response_json = response.json()
    if not "data" in response_json:
        raise Exception(response_json["message"])
    pprint(response_json)
    response_object = ResponseBody(**response_json)

    return response_type(**response_object.data)


class ResponseBody(Generic[T]):
    code: str
    message: str
    data: T

    def __init__(self, code: str, message: str, data: T):
        self.code = code
        self.message = message
        self.data = data
