import sys
import httpx
import functools
import logging

logger = logging.getLogger(__name__)

def handle_api_call_exceptions(func):
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
        except TypeError as e:
            logger.error(f"Type error: {e}")
        except Exception as e:
            logger.exception(f"An unexpected error occurred: {e}")
        finally:
            # Optionally, you can log the error or take other actions
            logger.error("API call completed with errors.")
        return None
    return wrapper