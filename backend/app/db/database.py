from sqlalchemy import create_engine
from app.core.config import settings

engine = create_engine(
        settings.DATABASE_URL, echo=True,
        pool_size=10,
        max_overflow=20,
        pool_timeout=30,
        pool_recycle=1800,
        pool_pre_ping=True)
