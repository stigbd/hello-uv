"""Test the main function."""

from fastapi import status
from fastapi.testclient import TestClient

from app import app


def test_get_root() -> None:
    """Should return 200 and a json body."""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World"}


def test_head_root() -> None:
    """Should return 200 and an empty body."""
    client = TestClient(app)
    response = client.head("/")
    assert response.status_code == status.HTTP_200_OK
    assert "content-type" not in response.headers
    assert response.headers["content-length"] == "0"
    assert response.text == ""
