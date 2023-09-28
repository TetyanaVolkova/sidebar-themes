from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(
    tags=["static"],
)

DATA = [
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Porsche",
"model": "Boxter",
"price": 72000
},
{
"make": "Toyota",
"model": "Celica",
"price": 35000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
},
{
"make": "Ford",
"model": "Mondeo",
"price": 32000
}
]

@router.get("/test/") 
def get_survey():
    return DATA