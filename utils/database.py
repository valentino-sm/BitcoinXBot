from contextlib import asynccontextmanager

from loguru import logger
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from utils import settings

# Explicit Cache On Hack for SQLAlchemy warning
from sqlmodel.sql.expression import Select, SelectOfScalar
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

db_engine = create_async_engine(
        f"{settings.db_driver}://{settings.db_user}:{settings.db_pass}@{settings.db_host}:{settings.db_port}/{settings.db_name}",
        echo=settings.debug, future=True,
        pool_size=10, max_overflow=9, pool_recycle=3600,
    )


async def db_init():
    async with db_engine.begin() as conn:
        import models
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


@asynccontextmanager
async def db_session() -> AsyncSession:
    async_session = scoped_session(sessionmaker( # noqa
        db_engine, class_=AsyncSession, expire_on_commit=False
    ))
    async with async_session() as session:
        session: AsyncSession
        try:
            yield session
        except BaseException as e:
            logger.error(f"An error has occured in runtime SQL query.")
            await session.rollback()
            raise e
