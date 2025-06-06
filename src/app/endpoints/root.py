"""Handler for the / endpoint."""

import logging

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

logger = logging.getLogger("app.endpoints.handlers")

router = APIRouter(tags=["root"])


INDEX_PAGE = """
<html>
    <head>
        <title>Lightspeed core service</title>
    </head>
    <body style='font-family: sans-serif;text-align:center;'>
        <h1>Lightspeed core service</h1>
        <img src="https://avatars.githubusercontent.com/u/204013222?s=400&u=47337cca0a4abbca5cfcc45fc20c7a2e82ac35e1&v=4" />
        <div><a href="docs">Swagger UI</a></div>
        <div><a href="redoc">ReDoc</a></div>
    </body>
</html>
"""


@router.get("/", response_class=HTMLResponse)
def root_endpoint_handler(_request: Request) -> HTMLResponse:
    """Handle request to the / endpoint."""
    logger.info("Serving index page")
    return HTMLResponse(INDEX_PAGE)
