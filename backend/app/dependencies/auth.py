# jwt验证
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database import get_db
from app.model.user import User
from app.utils.jwt import decode_access_token

# 通过OAuth2PasswordBearer自动从请求头中获取token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):   # depends()依赖注入
   try:
       payload = decode_access_token(token)

   except Exception:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="登录已失效，请重新登录")

   # 获取到用户id
   user_id = payload.get("user_id")
   if not user_id:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="无效的登录凭证")

   # 从数据库查询用户信息
   user = db.query(User).filter(User.id == user_id).first()
   if not user:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="用户不存在")

   if user.status == 0:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="账号已被禁用")

   return user

