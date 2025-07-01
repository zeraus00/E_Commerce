from contextlib import asynccontextmanager
from pathlib import Path

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from backend.config.settings import Settings

settings = Settings()

if settings.ENVIRONMENT == 'dev':
    sql_lite = Path(__file__).resolve().parent.parent.parent / 'dev.db'
    engine = create_async_engine(
        url=f'sqlite+aiosqlite:///{sql_lite}',
        connect_args={"check_same_thread": False}
    )
elif settings.ENVIRONMENT == 'prod':
    engine = create_async_engine(
        url=settings.DB_URL,

    )
else:
    raise Exception('No database selected!')

try:
    LocalSession = sessionmaker(
        class_=AsyncSession,
        bind=engine,
        autoflush=False,
        expire_on_commit=False
    )
except Exception as e:
    raise e


@asynccontextmanager
async def create_session() -> AsyncSession:
    async with LocalSession() as session:
        try:
            yield session
        except Exception as e:
            print(f'An error occurred: {e}')
            await session.rollback()