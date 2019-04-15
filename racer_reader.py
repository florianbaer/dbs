import pandas


class RacerReader(object):
    def __init__(self, path):
        self.path = path

    def parse_csv(self):
        csv = pandas.read_csv(self.path, ',', encoding="ISO-8859-1")
        # print(csv)
        print(list(csv.columns.values))
