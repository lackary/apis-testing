import sys
import httpx
import functools
import logging

logger = logging.getLogger(__name__)

def handle_base_exceptions_async(func):
    """
    Decorator to handle base exceptions.
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except TypeError as e:
            logger.error(f"Type error: {e}")
        except Exception as e:
            logger.exception(f"An unexpected error occurred: {e}")
            return None
    return wrapper

def handle_api_call_exceptions_async(func):
    """
    Decorator to handle API call exceptions.
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except httpx.RequestError as e:
            logger.error(f"API call failed: {e}")
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error occurred: {e}")
        except ValueError as e:
            logger.error(f"JSON parsing error: {e}")
        return None
    return wrapper