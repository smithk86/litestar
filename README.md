<img alt="StarLite logo" src="./starlite-logo.svg" width=100%, height="auto">

![PyPI - License](https://img.shields.io/pypi/l/starlite?color=blue)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/starlite)
![Discord](https://img.shields.io/discord/919193495116337154?color=blue&label=chat%20on%20discord&logo=discord)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)

# StarLite

StarLite is a light, opinionated and flexible ASGI API framework built on top
of [pydantic](https://github.com/samuelcolvin/pydantic) and [Starlette](https://github.com/encode/starlette).

## Installation

Using your package manager of choice:

```shell
pip install starlite
```

OR

```shell
poetry add starlite
```

OR

```shell
pipenv install starlite
```

You will also need an ASGI server such as [uvicorn](https://github.com/encode/uvicorn)
or [daphne](https://github.com/django/daphne/), e.g.:

```shell
pip install uvicorn
```

## Minimal Example

Define your data model using pydantic or any library based on it (see for example ormar, beanie, SQLModel etc.):

```python
# my_app/models/user.py

from pydantic import BaseModel, UUID4


class User(BaseModel):
    first_name: str
    last_name: str
    id: UUID4
```

You can alternatively use a dataclass, either the standard library one or the one from pydantic:

```python
# my_app/models/user.py
from uuid import UUID

# from pydantic.dataclasses import dataclass
from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    id: UUID
```

Define a Controller for your data model:

```python
# my_app/controllers/user.py
from pydantic import UUID4
from starlite.controller import Controller
from starlite.handlers import get, post, put, patch, delete
from starlite.types import Partial

from my_app.models import User


class UserController(Controller):
    path = "/users"

    @post()
    async def create(self, data: User) -> User:
        ...

    @get()
    async def get_users(self) -> list[User]:
        ...

    @patch()
    async def partial_update_user(self, data: Partial[User]) -> User:
        ...

    @put()
    async def bulk_update_users(self, data: list[User]) -> list[User]:
        ...

    @get(path="/{user_id:uuid}")
    async def get_user_by_id(self, user_id: UUID4) -> User:
        ...

    @delete(path="/{user_id:uuid}")
    async def delete_user_by_id(self, user_id: UUID4) -> User:
        ...

```

Import your controller into your application's entry-point and pass it to Starlite when instantiating your app:

```python
# my_app/main.py

from starlite import Starlite

from my_app.controllers.user import UserController

app = Starlite(route_handlers=[UserController])

```

To run you application, use an ASGI server such as uvicorn:

```shell
uvicorn my_app.main:app --host 0.0.0.0 --port "3000"
```

## Project and Status

This project was inspired by FastAPI, which also uses Starlette and pydantic as a basis, but with an intent of following
a different path:

1. The goal of this project is to become a community driven project. That is, not to have a single "owner" but rather a
   core team of maintainers that leads the project, as well as community contributors.
2. StarLite draws inspiration from NestJS - a contemporary TypeScript framework - which places opinions and patterns at
   its core. As such, the design of the API breaks from the Starlette design and instead offers an opinionated
   alternative- python OOP is extremely powerful and versatile. StarLite seeks to build on this by offering class based
   Controllers.

### Features and roadmap:

- [x] sync and async API endpoints
- [x] fast json serialization using [orjson](https://github.com/ijl/orjson)
- [x] class based controllers
- [x] decorators based configuration
- [x] rigorous typing and type inference
- [x] layered dependency injection
- [x] automatic OpenAPI schema generation
- [x] support for pydantic models and pydantic dataclasses
- [x] support for vanilla python dataclasses
- [x] extended testing support
- [ ] detailed documentation
- [ ] built-in redoc based OpenAPI UI
- [ ] request interceptors
- [ ] route guards
- [ ] schemathesis integration

### Contributing

StarLite is open to contributions big and small. You can always [join our discord](https://discord.gg/X3FJqy8d2j) server to discuss contributions and
project maintenance. For guidelines on how to contribute, please see [the contribution guide](CONTRIBUTING.md).
