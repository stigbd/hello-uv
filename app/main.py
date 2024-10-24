"""Main module for the FastAPI application."""

from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    """Return a simple message."""
    return {"message": "Hello World"}


@app.head("/")
async def head_root() -> Response:
    """Return empty body."""
    return Response()
