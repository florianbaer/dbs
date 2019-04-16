import pandas
from pandas._libs.parsers import basestring

class StatusReader(object):
    def __init__(self, path):
        self.path = path

    def parse_csv(self):
        self.csv = pandas.read_csv(self.path, ',', encoding="ISO-8859-1")
        print(list(self.csv.columns.values))
        self.csv.set_index('statusId', inplace=True)

    def get_status(self, status_id):
        row = self.csv.loc[[status_id], :]
        return row['status'].values[0]
