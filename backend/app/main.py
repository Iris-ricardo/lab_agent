from fastapi import FastAPI

from app.api import api
from app.database import Base, engine

Base.metadata.create_all(bind=engine) #自动创建数据库
app = FastAPI()
app.include_router(api) # 添加api.router

@app.get("/")
def read_root():
    return {"message": "FastAPI工程测试正常"}