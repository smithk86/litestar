from random import randint

from pydantic import BaseModel

from litestar import Litestar, Response, Router, get
from litestar.datastructures import Cookie


class Resource(BaseModel):
    id: int
    name: str


@get(
    "/resources",
    response_cookies=[
        Cookie(
            key="Random-Cookie",
            description="a random number in the range 100 - 1000",
            documentation_only=True,
        )
    ],
)
def retrieve_resource() -> Response[Resource]:
    return Response(
        Resource(
            id=1,
            name="my resource",
        ),
        cookies=[Cookie(key="Random-Cookie", value=str(randint(100, 1000)))],
    )


def after_request_handler(response: Response) -> Response:
    response.set_cookie(key="Random-Cookie", value=str(randint(1, 100)))
    return response


router = Router(
    path="/router-path",
    route_handlers=[retrieve_resource],
    after_request=after_request_handler,
    response_cookies=[
        Cookie(
            key="Random-Cookie",
            description="a random number in the range 1 - 100",
            documentation_only=True,
        )
    ],
)

app = Litestar(route_handlers=[router])
