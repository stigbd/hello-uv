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
% uv run pytest
```

As far as I know, at the moment there is no way to run all of the above commands in one go. But see <https://github.com/astral-sh/uv/issues/5903> for a discussion on this.

## Add FastAPI

```zsh
% uv add fastapi --extra standard
% uv run fastapi dev
```

## Useful uv commands

```zsh
% uv --help
% uv self update # updates uv to the latest version
% uv init && uv add -r requirements.txt # initializes a new project and installs dependencies from requirements.txt
```

## References

- [uv](https://docs.astral.sh/uv)
- [fastapi](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
