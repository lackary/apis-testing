import pytest
import httpx
from src.utils.decorators import handle_base_exceptions_async, handle_api_call_exceptions_async

@pytest.mark.asyncio
async def test_handle_base_exceptions_async_type_error(caplog):
    @handle_base_exceptions_async
    async def func():
        raise TypeError("type error!")
    with caplog.at_level("ERROR"):
        result = await func()
    assert result is None
    assert "Type error: type error!" in caplog.text

@pytest.mark.asyncio
async def test_handle_base_exceptions_async_other_exception(caplog):
    @handle_base_exceptions_async
    async def func():
        raise RuntimeError("runtime error!")
    with caplog.at_level("ERROR"):
        result = await func()
    assert result is None
    assert "An unexpected error occurred: runtime error!" in caplog.text

@pytest.mark.asyncio
async def test_handle_base_exceptions_async_success():
    @handle_base_exceptions_async
    async def func():
        return 123
    result = await func()
    assert result == 123

@pytest.mark.asyncio
async def test_handle_api_call_exceptions_async_request_error(caplog):
    @handle_api_call_exceptions_async
    async def func():
        raise httpx.RequestError("request failed")
    with caplog.at_level("ERROR"):
        result = await func()
    assert result is None
    assert "API call failed: request failed" in caplog.text

@pytest.mark.asyncio
async def test_handle_api_call_exceptions_async_http_status_error(caplog):
    @handle_api_call_exceptions_async
    async def func():
        raise httpx.HTTPStatusError("bad status", request=None, response=None)
    with caplog.at_level("ERROR"):
        result = await func()
    assert result is None
    assert "HTTP error occurred: bad status" in caplog.text

@pytest.mark.asyncio
async def test_handle_api_call_exceptions_async_value_error(caplog):
    @handle_api_call_exceptions_async
    async def func():
        raise ValueError("bad value")
    with caplog.at_level("ERROR"):
        result = await func()
    assert result is None
    assert "JSON parsing error: bad value" in caplog.text

@pytest.mark.asyncio
async def test_handle_api_call_exceptions_async_success():
    @handle_api_call_exceptions_async
    async def func():
        return 42
    result = await func()
    assert result == 42