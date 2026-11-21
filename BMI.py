from fastapi import FastAPI, Path, HTTPException, Query
from typing import Annotated
from pydantic import BaseModel,Field
import json

app=FastAPI()

class Patient(BaseModel):
    name:Annotated[str,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ]
    city:str
    age:int
    gender:str
    height:float
    weight:float