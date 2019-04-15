import pandas


class RaceResult(object):
    def __init__(self, result_id, race_id, position_order, points, status):
        self.points = points
        self.positionOrder = position_order
        self.raceId = race_id
        self.resultId = result_id
        self.status = status


class Result(object):
    def __init__(self, driver, constructor, race_result):
        self.race_result = race_result
        self.constructor = constructor
        self.driver = driver


class ResultsReader(object):
    def __init__(self, path, driver_reader, constructor_reader):
        self.constructor_reader = constructor_reader
        self.driver_reader = driver_reader
        self.path = path

    def parse_csv(self):
        self.csv = pandas.read_csv(self.path, ',', encoding="ISO-8859-1")
        # print(csv)
        print(list(self.csv.columns.values))
        races = []
        for index, row in self.csv.iterrows():
            races.append(Result(self.driver_reader.get_driver(row['driverId']),
                                self.constructor_reader.get_constructor(row['constructorId']),
                                RaceResult(row['resultId'], row['raceId'],
                                           row['positionOrder'],
                                           row['points'], row['statusId'])))
        return races
