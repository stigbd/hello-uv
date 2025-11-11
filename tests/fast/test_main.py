"""Test the main function."""

import pytest
from fastapi import status
from httpx import ASGITransport, AsyncClient

from app import app


@pytest.fixture
def anyio_backend() -> str:
    """Use the asyncio backend for the anyio fixture."""
    return "asyncio"


@pytest.mark.anyio
async def test_get_root() -> None:
    """Should return 200 and a json body."""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        response = await ac.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello, World!"}


@pytest.mark.anyio
async def test_head_root() -> None:
    """Should return 200 and an empty body."""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        response = await ac.head("/")
    assert response.status_code == status.HTTP_200_OK
    assert "content-type" not in response.headers
    assert response.headers["content-length"] == "0"
    assert response.text == ""
