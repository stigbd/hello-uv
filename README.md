# hello-uv

A small reference python project to demonstrate how to use [uv](https://docs.astral.sh/uv) for an application project.

## Create a new project

This project was created using the following commands:

```zsh
% uv init --app hello-uv
% cd hello-uv
% uv run hello.py
Hello world from hello.py!
```

## Install and run formatter, linter, type checker, and test runner

```zsh
% uv add ruff --dev
% uv add pyright --dev
% uv add pytest --dev
% uv add pytest-cov --dev
```

Observe the relevant configurations in pyproject.toml.

```zsh
% uv run ruff format
% uv run ruff check --fix
% uv run pyright
% uv run pytest
```

### Dependency checker

To check for unused or missing dependencies, I use [deptry](https://deptry.com/):

```zsh
% uv add deptry --dev
% uv run deptry .
```

### Task runner

As far as I know, at the moment there is no way to run all of the above commands in one go. But see <https://github.com/astral-sh/uv/issues/5903> for a discussion on this.
Until this is resolved, I have used [Poe the Poet](https://github.com/nat-n/poethepoet)

```zsh
% uv add poethepoet --dev
```

In `pyproject.toml` I have added the following:

```toml
[tool.poe.tasks]
fmt = "uv run ruff format"
lint = "uv run ruff check --fix"
pyright = "uv run pyright"
test = "uv run pytest"
check-deps = "uv run deptry ."
release = [
    "lint",
    "pyright",
    "check-deps",
    "test",
]
```

To run all of the above commands in one go, I can now use the following command:

```zsh
% uv run poe release
```

## Add FastAPI

Run in development mode:

```zsh
% uv add fastapi --extra standard
% uv run fastapi dev
```

Run with Uvicorn:

```zsh
% uv run uvicorn app:app
```

Build and run the docker image:

```zsh
% docker build -t hello-uv .
% docker run --name hello-uv -d -p 8080:8080 hello-uv
```

Stop the docker container:

```zsh
% docker stop hello-uv
```

Build and run with docker compose:

```zsh
% docker compose up --build -d
% docker compose logs -f
% docker compose down
```

## Debug

To debug the application, you can add `breakpoint()` in the code and run the application.
This method shold also work when running tests. In the latter scenario, you need to set `--capture=no` in the pytest command.

## Useful uv commands

```zsh
% uv --help
% uv self update # updates uv to the latest version
% uv init && uv add -r requirements.txt # initializes a new project and installs dependencies from requirements.txt
```

## References

- [uv](https://docs.astral.sh/uv)
- [fastapi](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
