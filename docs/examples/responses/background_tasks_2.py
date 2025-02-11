import logging
from typing import Dict

from litestar import Litestar, get
from litestar.background_tasks import BackgroundTask

logger = logging.getLogger(__name__)


async def logging_task(identifier: str, message: str) -> None:
    logger.info("%s: %s", identifier, message)


@get("/", background=BackgroundTask(logging_task, "greeter", message="was called"))
def greeter() -> Dict[str, str]:
    return {"hello": "world"}


app = Litestar(route_handlers=[greeter])
