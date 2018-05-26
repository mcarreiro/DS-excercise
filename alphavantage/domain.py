class Currency:

    def __init__(self, name):
        self.name = name

    def validate(self):
        pass

    def __str__(self):
        return self.name


class CurrencyDaily:

    def __init__(self, currency_name, date, open_value, high, low, close, volume, market_cap, open_usd, high_usd, low_usd,
                 close_usd):
        self.currency_name = currency_name
        self.date = date
        self.open = open_value
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.market_cap = market_cap
        self.open_usd = open_usd
        self.high_usd = high_usd
        self.low_usd = low_usd
        self.close_usd = close_usd


    def validate(self):
        pass