from fastapi import APIRouter, Request
import boto3
import json
import os

router = APIRouter(
    tags=["static"],
)

#@cache(expire=300)
@router.get("/test/") 
def get_survey(request: Request) -> str:
    return 'Test!'