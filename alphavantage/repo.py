from rest_client import RestClient
import datetime
from alphavantage.domain import CurrencyDaily
from alphavantage.domain import Currency


class AlphaVantageCurrencyDailyRepo:
    missing_currency_url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=%s&market=%s&apikey=demo'

    currency_daily_key = 'Time Series (Digital Currency Daily)'

    market = 'CNY'

    date_format = "%Y-%m-%d"

    keys = ['close', 'open', 'high', 'low', 'market cap']
    volume = 'volume'

    usd_currency = Currency('USD')

    def __init__(self):
        self.rest_client = RestClient()

    def get_currency_dailies_by_currency_and_date_range(self, currency, date_from, date_to):
        json_response = self.get_by_currency(currency)
        json_response = self.filterByDateRange(json_response, date_from, date_to)
        return self.transform(json_response, currency)

    def filterByDateRange(self, json_response, date_from, date_to):
        json_response_final = {}
        delta = date_to - date_from
        date_range = [date_to - datetime.timedelta(days=x) for x in range(delta.days + 1)]
        for date in date_range:
            string_date = date.strftime(self.date_format)
            json_response_final[string_date] = json_response[string_date]

        return json_response_final

    def transform(self, json_response, currency):
        curreny_dailies = []
        for string_date, currency_daily_json in json_response.items():
            currency_daily_mapping = {}
            for attribute, value in currency_daily_json.items():
                key = self.get_attribute_name_by_currency(attribute)
                if key != '':
                    currency_daily_mapping[key] = value

            date = datetime.datetime.strptime(string_date, self.date_format)
            curreny_dailies.append(CurrencyDaily(currency.name,
                                                 date,
                                                 currency_daily_mapping['open'],
                                                 currency_daily_mapping['high'],
                                                 currency_daily_mapping['low'],
                                                 currency_daily_mapping['close'],
                                                 currency_daily_mapping['volume'],
                                                 currency_daily_mapping['market cap_usd'],
                                                 currency_daily_mapping['open_usd'],
                                                 currency_daily_mapping['high_usd'],
                                                 currency_daily_mapping['low_usd'],
                                                 currency_daily_mapping['close_usd'],
                                                 ))

        return curreny_dailies

    def get_by_currency(self, currency):
        url_by_currency = self.missing_currency_url % (currency.name, self.market)
        json_response = self.rest_client.get(url_by_currency)

        return json_response[self.currency_daily_key]

    def get_attribute_name_by_currency(self, attribute):
        if self.usd_currency.name in attribute:
            for key in self.keys:
                if key in attribute:
                    return key + "_usd"
        elif self.market in attribute:
            for key in self.keys:
                if key in attribute:
                    return key
        elif self.volume in attribute:
            return self.volume
        else:
            return ''
