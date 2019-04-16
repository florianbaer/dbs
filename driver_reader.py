import pandas
from pandas._libs.parsers import basestring


class Driver(object):
    def __init__(self, driver_id, forename, surname, nationality):
        self.nationality = nationality
        self.surname = surname
        self.forename = forename
        self.driver_id = driver_id


class DriverReader(object):
    def __init__(self, path):
        self.path = path

    def parse_csv(self):
        self.csv = pandas.read_csv(self.path, ',', encoding="ISO-8859-1")
        print(list(self.csv.columns.values))
        self.csv.set_index('driverId', inplace=True)

    def get_driver(self, driver_id):
        row = self.csv.loc[[driver_id], :]
        #print(row['forename'])
        #print(str(row['forename']))
        return Driver(driver_id, row['forename'].values[0], row['surname'].values[0],
                      row['nationality'].values[0])
