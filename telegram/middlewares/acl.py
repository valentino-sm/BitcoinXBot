from typing import Optional

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.users import User
from utils.database import db_session
from utils.async_lru import alru_cache


class ACLMiddleware(BaseMiddleware):

    async def setup_chat(self, user: types.User, data: dict):

        user_id = user.id
        username = user.username

        async with db_session() as session:
            session: AsyncSession
            user = (await session.execute(select(User).where(User.userid == user_id))).scalar()
            if not user:
                user = User(userid=user_id, username=username)
                session.add(user)
                await session.commit()
                await session.refresh(user)
            logger.debug(user)
            return user

    async def on_pre_process_message(self, message: types.Message, data: dict):
        data["user"] = await self.setup_chat(message.from_user, data)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        data["user"] = await self.setup_chat(query.from_user, data)
