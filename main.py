from fastapi import FastAPI

import api
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api.router, tags=['todo_app'])
