from typing import Dict
from fastapi import Request

def get_x_api_key(http_request: Request):
    x_api_key = http_request.headers.get("x-api-key")
    if not x_api_key:
        x_api_key = http_request.headers.get("authorization")
    return x_api_key

def get_custom_headers(http_request: Request) -> Dict[str, str]:
    custom_headers = {}
    custom_key = {
        "x-api-key",
        "authorization",
        "anthropic-version",
        "user-agent",
    }
    for key, value in http_request.headers.items():
        if key in custom_key:
            custom_headers[key] = value
    return custom_headers