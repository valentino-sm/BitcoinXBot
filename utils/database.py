from gino import Gino

from utils import settings, logging

db = Gino()


async def db_init():
    await db.set_bind(
        f"{settings.db_driver}://{settings.db_user}:{settings.db_pass}@{settings.db_host}:{settings.db_port}/{settings.db_name}",
        echo=settings.debug, pool_recycle=3600,
    )
    if settings.debug:
        logging.clear_handlers()
    await db.gino.create_all()


async def db_close():
    await db.pop_bind().close()