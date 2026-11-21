# 解析jwt token
from datetime import datetime, timedelta, timezone
import jwt
from app.config import settings


def create_access_token(user_id: str) -> str:
    # token过期时间
    expires = datetime.now(timezone.utc) + timedelta(days = settings.JWT_EXPIRE_HOURS)
    # token负载
    payload = {"user_id": user_id, "exp": expires}
    # 返回token的签名编码
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm = settings.JWT_ALGORITHM)

def decode_access_token(token: str):
    # 与创建token相反的步骤
    return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])





