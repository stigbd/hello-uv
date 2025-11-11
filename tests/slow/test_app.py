"""Test module for the root resource."""

import time
from http import HTTPStatus
from pathlib import Path
from typing import Any

import httpx
import pytest


def is_responsive(url: str) -> bool | None:
    """Check if container is ready."""
    time.sleep(2)  # sleep a little, to let the docker container start
    try:
        response = httpx.get(url, timeout=30)
        if response.status_code == HTTPStatus.OK:
            return True
    except ConnectionError:
        return False


@pytest.fixture(scope="session")
def http_service(docker_ip: str, docker_services: Any) -> str:
    """Ensure that HTTP service is up and responsive."""
    # `port_for` takes a container port and returns the corresponding host port
    port = docker_services.port_for("hello-uv", 8080)
    url = f"http://{docker_ip}:{port}"
    docker_services.wait_until_responsive(
        timeout=30.0,
        pause=0.1,
        check=lambda: is_responsive(url),
    )
    return url


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig: Any) -> Any:
    """Override default location of docker compose file."""
    return Path(str(pytestconfig.rootdir), "compose.yaml")


@pytest.fixture
def anyio_backend() -> str:
    """Use the asyncio backend for the anyio fixture."""
    return "asyncio"


@pytest.mark.anyio
async def test_get_root(http_service: str) -> None:
    """Should return 200 OK and a json body."""
    async with httpx.AsyncClient() as client:
        response = await client.get(http_service)

    assert response.status_code == HTTPStatus.OK
    assert response.headers["Content-type"] == "application/json"

    body = response.json()
    assert body["message"] == "Hello World!"


@pytest.mark.anyio
async def test_head_root(http_service: str) -> None:
    """Should return 200 OK and no body."""
    async with httpx.AsyncClient() as client:
        response = await client.head(http_service)

    assert response.status_code == HTTPStatus.OK
    assert "Content-type" not in response.headers
    assert response.text == ""
