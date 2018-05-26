import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


class CurrencyDailiesPlotter:

    date_field_name = 'date'

    def get_plot_by_date(self, csv_file_name, headers, y_name, point_tagger):
        df = pd.read_csv(csv_file_name, skiprows=[0], names=headers)

        df[self.date_field_name] = df[self.date_field_name].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))

        x = df[self.date_field_name]
        y = df[y_name]

        # plot
        plt.plot(x, y)

        #plot anomalies
        df = point_tagger(df,y_name)
        y = df['anomalies']
        plt.plot(x, y)

        # beautify the x-labels
        plt.gcf().autofmt_xdate()

        plt.show(style='o')
