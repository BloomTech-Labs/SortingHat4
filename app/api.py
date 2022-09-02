from datetime import datetime
from typing import Dict, Optional

import pytz
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.data_models import Payload
from app.payload import example_payload
from app.sorting_hat import sorting_hat
from app.logger import MongoDB

API = FastAPI(
    title="SortingHat4",
    version="4.4.2",
    docs_url="/",
    description="<h2>Phoenix</h2>"
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
        "timestamp": datetime.now(pytz.timezone('US/Pacific')).isoformat(),
    }


@API.post("/sortinghat")
async def sortinghat(payload: Payload = example_payload()) -> Payload:
    try:
        result: Payload = sorting_hat(payload)
        API.logger.insert({
            "metadata": await info(),
            "before": {
                "projects": list(map(vars, payload.projects)),
                "learners": list(map(vars, payload.learners)),
            },
            "after": {
                "projects": list(map(vars, result.projects)),
                "learners": list(map(vars, result.learners)),
            },
        })
        return result
    except Exception as error:
        API.logger.insert({
            "metadata": await info(),
            "payload": payload,
            "error": error,
        })


@API.get("/schema")
async def payload_schema():
    return Payload.schema()
