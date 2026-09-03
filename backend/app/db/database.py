from core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

engine = create_async_engine(
        settings.DATABASE_URL, echo=True,
        pool_size=10,
        max_overflow=20,
        pool_timeout=5,
        pool_recycle=1800,
        pool_pre_ping=True)


AsyncSessionLocal = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)