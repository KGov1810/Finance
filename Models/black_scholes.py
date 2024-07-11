import math

from scipy.stats import norm


class BlackScholes:

    def __init__(self, **kwargs):
        self.strike = kwargs.get("strike")
        self.spot = kwargs.get("spot")
        self.maturity = kwargs.get("maturity")
        self.risk_free = kwargs.get("risk_free")
        self.sigma = kwargs.get("sigma")

    def _black_scholes_elements(self):
        """Function to calculate d1 and d2 for black scholes"""
        d1 = (math.log(self.spot / self.strike) + (self.risk_free + (self.sigma**2)/2) * self.maturity) / (self.sigma * math.sqrt(self.maturity))
        d2 = d1 - self.sigma * math.sqrt(self.maturity)
        return d1, d2

    def calculate_call(self):
        """Function to calculate the call"""
        d1, d2 = self._black_scholes_elements()
        call_price = self.spot * norm.cdf(d1) - self.strike * math.exp(-self.risk_free * self.maturity) * norm.cdf(d2)
        return call_price

    def calculate_put(self):
        """Function to calculate the put"""
        d1, d2 = self._black_scholes_elements()
        put_price = self.strike * math.exp(-self.risk_free * self.maturity) * norm.cdf(-d2) - self.spot * norm.cdf(-d1)
        return put_price
