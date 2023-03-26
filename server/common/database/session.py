from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

from server.config.settings import settings

SQLALCHEMY_URI_OBJECT = URL.create(
    settings.DATABASE_DRIVER,
    username=settings.DATABASE_USER,
    password=settings.DATABASE_PASS,  # plain (unescaped) text
    host=settings.DATABASE_HOST,
    port=settings.DATABASE_PORT,
    database=settings.DATABASE_NAME,
)

DATABASE_URI = settings.DATABASE_URI or SQLALCHEMY_URI_OBJECT

engine = create_engine(DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
