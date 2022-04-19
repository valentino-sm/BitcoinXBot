from decimal import Decimal

from .account import account_ctx, AccountData
from models.users import User as UserModel


class User:
    @staticmethod
    async def create_default() -> UserModel:
        current_account = account_ctx.get()
        account_data: AccountData = await current_account.get_data()
        user = UserModel(
            userid=account_data.userid,
            username=account_data.username,
            lang=account_data.lang,
            BTC=Decimal("0.00010000"),
            USD=Decimal("1000"),
            RUB=Decimal("500"),
            EUR=Decimal("1"),
            bot=await current_account.get_me(),
        )
        await user.create()
        return user

    @staticmethod
    # @AsyncTTL(time_to_live=3600)
    async def get_from_id(userid: int):
        return await UserModel.query.where(UserModel.userid == userid).gino.first()

    @staticmethod
    async def get_current() -> UserModel:
        user = await User.get_from_id(account_ctx.get().get_userid())
        if not user:
            user = await User.create_default()
        return user
