import uuid

from sqlalchemy import Column, DateTime, Integer, UUID, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class BaseModel:
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    gid = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())

    __name__: str

    # Generate __tablename__ automatically
    # Generate table name will be plural
    @declared_attr
    def __tablename__(cls) -> str:
        return "".join([cls.__name__.lower(), "s"])
