import pandas
from pandas._libs.parsers import basestring


class Circuit(object):
    def __init__(self, id, name, country, location):
        self.id = id
        self.location = location
        self.country = country
        self.name = name


class CircuitsReader(object):
    def __init__(self, path):
        self.path = path

    def parse_csv(self):
        self.csv = pandas.read_csv(self.path, ',', encoding="ISO-8859-1")
        print(list(self.csv.columns.values))
        self.csv.set_index('circuitId', inplace=True)

    def get_circuit(self, circuit_id):
        row = self.csv.loc[[circuit_id], :]
        return Circuit(circuit_id, row['name'].values[0], row['country'].values[0], row['location'].values[0])
