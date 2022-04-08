from models.rates import Rates as RatesModel
from utils.misc import logic_mult, logic_div


class Rates(RatesModel):
    @property
    def BTC_RUB(self):
        return logic_mult(self.USD_RUB, self.BitMEX_BTC_USD)

    @property
    def ETH_RUB(self):
        return logic_mult(self.USD_RUB, self.BitMEX_ETH_USD)

    @property
    def BTC_EUR(self):
        return logic_div(self.BTC_RUB, self.EUR_RUB)

    @property
    def BTC_CNY(self):
        return logic_div(self.BTC_RUB, self.CNY_RUB)

    @property
    def CNY_USD(self):
        return logic_div(self.CNY_RUB, self.USD_RUB)

