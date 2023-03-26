from sqlalchemy import Column, String, Boolean, DateTime

from server.common.database.base import BaseModel


class User(BaseModel):
    first_name = Column(String(length=128), nullable=True)
    last_name = Column(String(length=128), nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String(length=128), nullable=False)
    is_active = Column(Boolean, default=False)
    last_login = Column(DateTime(timezone=True), nullable=True)
