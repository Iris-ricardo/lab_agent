from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class User(Base):
    __tablename__ = "user"
    __table_args__ = {"comment":"用户信息表"}

#   定义字段,注意string类型需要指定长度，最好设置长一点，因为utils/password()中采取hash_password()函数对用户信息进行加密，若长度不够会报错
    username:Mapped[str] = mapped_column(String(255), comment="账号", nullable=False)
    password:Mapped[str] = mapped_column(String(255), comment="密码", nullable=False)
    name: Mapped[str] = mapped_column(String(255), comment="名字", nullable=False)
    role: Mapped[str] = mapped_column(String(255), comment="角色：student-学生， admin-管理员", nullable=False)
    email: Mapped[str | None] = mapped_column(String(255), comment="邮箱", nullable=True)
    phone: Mapped[str | None] = mapped_column(String(255), comment="手机号", nullable=True)
    avatar: Mapped[str | None] = mapped_column(String(255), comment="头像", nullable=True)
    status: Mapped[int | None] = mapped_column(default=1, comment="状态：0-禁用， 1-正常")

