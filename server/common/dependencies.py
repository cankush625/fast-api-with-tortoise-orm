from typing import Generator

from server.common.database.session import SessionLocal


# This can be done using middleware as well. Only disadvantage with middleware
# is that it will try to create database session even if the request does not
# require a database session
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
