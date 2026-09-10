from starlette.middleware.base import BaseHTTPMiddleware


class MyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
