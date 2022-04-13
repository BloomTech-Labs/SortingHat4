import datetime
from typing import Dict, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.data_models import Payload
from app.hat_trick import hat_trick
from app.logger import MongoDB

API = FastAPI(
    title="SortingHat4",
    version="4.1.0rc2",
    docs_url="/",
    description="<h2>Truffle Shuffle Edition</h2>"
)
API.logger = MongoDB()
API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.get("/info")
async def info():
    return {
        "ds_api": {
            "platform": "FastAPI",
            "title": API.title,
            "version": API.version,
        },
        "logger": API.logger.info,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


@API.post("/logs")
async def logs(query: Optional[Dict] = None):
    return list(API.logger.find_all(query))


@API.post("/sortinghat")
async def sortinghat(payload: Payload) -> Payload:
    result: Payload = hat_trick(payload)
    API.logger.insert({
        "metadata": await info(),
        "projects": list(map(vars, result.projects)),
        "learners": list(map(vars, result.learners)),
    })
    return result
