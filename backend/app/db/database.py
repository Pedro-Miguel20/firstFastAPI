from app.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
        settings.DATABASE_URL, echo=True,
        pool_size=15,
        max_overflow=15,
        pool_timeout=5,
        pool_recycle=1800,
        pool_pre_ping=True)


AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)