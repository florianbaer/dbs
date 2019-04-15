import pandas
from pandas._libs.parsers import basestring


class Constructor(object):
    def __init__(self, constructor_id, name, nationality):
        self.nationality = nationality
        self.name = name
        self.constructor_id = constructor_id


class ConstructorReader(object):
    def __init__(self, path):
        self.path = path

    def parse_csv(self):
        self.csv = pandas.read_csv(self.path, ',', encoding="ISO-8859-1")
        # print(csv)
        # print(list(self.csv.columns.values))

    def get_constructor(self, constructor_id):
        row = self.csv.loc[self.csv['constructorId'] == constructor_id]
        return Constructor(row['constructorId'].values[0], row['name'].values[0], row['nationality'].values[0])
