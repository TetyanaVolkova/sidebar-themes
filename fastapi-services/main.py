from fastapi import FastAPI, Request
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware

from routers import test
import time

app = FastAPI()
app.include_router(test.router)
origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
Start Cache
"""
@cache()
async def get_cache():
    return 1

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())
"""
End Cache
"""

""" 
Sart Middleware
"""
# Note, last listed is called first! 

# app.add_middleware(HTTPSRedirectMiddleware) # todo hook up to environment variable to force https
app.add_middleware(GZipMiddleware, minimum_size=1000)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


"""
End Middleware
"""



