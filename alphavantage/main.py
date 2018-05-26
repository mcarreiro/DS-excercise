import datetime

from file_saver import CSVFileSaver
from alphavantage.repo import AlphaVantageCurrencyDailyRepo
from alphavantage.domain import Currency
from alphavantage.plotter import CurrencyDailiesPlotter
from alphavantage import anomalies_detector

date_from_string = '2018-04-25'
date_to_string = '2018-05-25'
currency_name = 'BTC'
file_name = '/Users/mcarreiro/Downloads/a.csv'
headers = ['currency','date','open','high','low','close','volume','market_cap','open_usd','high_usd','low_usd','close_usd']

date_format = AlphaVantageCurrencyDailyRepo.date_format

date_from = datetime.datetime.strptime(date_from_string, date_format)
date_to = datetime.datetime.strptime(date_to_string, date_format)
currency = Currency(currency_name)

alpha_vantage_currency_daily_repo = AlphaVantageCurrencyDailyRepo()
csv_file_saver = CSVFileSaver()
plotter = CurrencyDailiesPlotter()

currency_dailies = alpha_vantage_currency_daily_repo.get_currency_dailies_by_currency_and_date_range(currency, date_from, date_to)

csv_file_saver.save(file_name,currency_dailies)

plotter.get_plot_by_date(file_name, headers, 'open', anomalies_detector.detect_by_variable_by_z_score)











