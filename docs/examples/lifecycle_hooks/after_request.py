from typing import Dict

from litestar import Litestar, MediaType, Response, get


async def after_request(response: Response) -> Response:
    if response.media_type == MediaType.TEXT:
        return Response({"message": response.body.decode()})
    return response


@get("/hello")
async def hello() -> str:
    return "Hello, world"


@get("/goodbye")
async def goodbye() -> Dict[str, str]:
    return {"message": "Goodbye"}


app = Litestar(route_handlers=[hello, goodbye], after_request=after_request)


# run: /hello
# run: /goodbye
