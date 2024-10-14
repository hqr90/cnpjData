# cnpjData/__init__.py

from .client import CNPJAPIClient
from exceptions import APIException, RateLimitException

__all__ = ["CNPJAPIClient", "APIException", "RateLimitException"]
