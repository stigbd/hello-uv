FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
ADD . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen

# Expose the application port.
EXPOSE 8080

# Run the application.
CMD ["/app/.venv/bin/uvicorn", "app:app",  "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]
