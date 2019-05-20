import pandas


class RaceResult(object):
    def __init__(self, Id, race, position_order, points, constructor, driver, status, racename):
        self.points = points
        self.positionOrder = position_order
        self.race = race
        self.Id = Id
        self.status = status
        self.constructor = constructor
        self.driver = driver
        self.racename = racename

class ResultsReader(object):
    def __init__(self, path, driver_reader, constructor_reader, status_reader, results_reader):
        self.status_reader = status_reader
        self.constructor_reader = constructor_reader
        self.driver_reader = driver_reader
        self.results_reader = results_reader
        self.path = path

    def parse_csv(self):
        self.csv = pandas.read_csv(self.path, ',', encoding="ISO-8859-1")
        # print(csv)

        # self.csv.set_index('resultId', inplace=True)
        print(list(self.csv.columns.values))
        races = []
        for index, row in self.csv.iterrows():
            races.append(RaceResult("result/" + str(row['resultId']),
                                    row['raceId'],
                                    row['positionOrder'],
                                    row['points'],
                                    self.constructor_reader.get_constructor(row['constructorId']),
                                    self.driver_reader.get_driver(row['driverId']),
                                    self.status_reader.get_status(row['statusId']),
                                    self.results_reader.get_name_by_id(row['raceId'])))
        return races
