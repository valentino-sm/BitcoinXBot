from typing import Optional

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from models.users import User
from utils.database import db_session
from utils.async_lru import alru_cache


class ACLMiddleware(BaseMiddleware):

    @alru_cache
    async def setup_chat(self, user: types.User):
        user_id = user.id
        username = user.username

        async with db_session() as session:
            session: AsyncSession
            user = (await session.execute(select(User).where(User.userid == user_id))).first()
            if user is None:
                user = User(userid=user_id, username=username)
                session.add(user)
                await session.commit()
                await session.refresh(user)

            return user

    async def on_pre_process_message(self, message: types.Message, data: dict):
        data["user"] = await self.setup_chat(message.from_user)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        data["user"] = await self.setup_chat(query.from_user)
