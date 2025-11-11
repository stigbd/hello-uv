"""Main module for the FastAPI application."""

from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()


class Greeting(BaseModel):
    """A simple greeting class."""

    message: str


@app.get("/")
async def root() -> Greeting:
    """Return a simple message."""
    return Greeting(message="Hello, World!")


@app.head("/")
async def head_root() -> Response:
    """Return empty body."""
    return Response()
