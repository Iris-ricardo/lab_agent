from datetime import datetime
from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column

from app.config import settings

engine = create_engine(settings.DATABASE_URL)

# 数据库session会话的连接工厂
SessionLocal = sessionmaker(bind = engine,autoflush = False)

# 会话管理
def get_db():
    db = SessionLocal(bind = engine) # 调用工厂创建会话
    try:
        yield db
    finally:
        db.close()

# 定义基础类
class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement = True,comment = '主键id')

    create_time:Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, comment="创建时间")

    update_time:Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')