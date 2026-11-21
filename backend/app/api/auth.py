# 权限操作部分
from fastapi import APIRouter, Depends, FastAPI
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.user import User
from app.schemas.auth import LoginRequest
from app.schemas.user import UserResponse
from app.utils.password import verify_password
from app.utils.jwt import create_access_token

# 定义api应用
router = APIRouter(prefix='/auth', tags=['权限验证'])
@router.post('/login')
def login(data: LoginRequest , db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username==data.username).first()

    # 判断账号密码
    if user is None or not verify_password(data.password, user.password):
        return {"code": "400",
                "message": "账号或密码错误"
                }
    # 判断账号状态
    if user.status == 0:
        return {
            "code": "403",
            "message": "账号已被禁用"
        }
    # 生成token
    token = create_access_token(user.id)

    # 返回token和用户信息
    return {"code": "200",
            "message": "确认通过",
            "data" : {"token": token, "user": UserResponse.model_validate(user)}
            }










