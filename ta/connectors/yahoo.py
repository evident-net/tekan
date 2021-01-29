import datetime as datetime

from pandas_datareader import data

from ta.mdl import DataSource


class YahooDataSource(DataSource):
    def __init__(self, id, range_start=None, range_end=None):
        super(YahooDataSource, self).__init__(id)
        self.range_start = range_start if range_start else datetime.datetime.today() - datetime.timedelta(days=2)
        self.range_end = range_end if range_end else datetime.date.today(),

    def load(self):
        self.data_frame = data.DataReader(self.id, 'yahoo', self.range_start, self.range_end)