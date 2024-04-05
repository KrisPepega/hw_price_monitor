from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from core import settings

db_url = f"{settings.db_dialect}+{settings.db_connector}://{settings.db_user}:{settings.db_passwd}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

async_engine = create_async_engine(db_url, echo=True, future=True)


async def get_async_db() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
