# 给登陆接口设置入参
from pydantic import BaseModel

class LoginRequest(BaseModel):  #将前端json解析成python回传后端进行验证
    username: str
    password: str