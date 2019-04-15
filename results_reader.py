import pandas

class Result(object):
    def __init__(self, result_id, race_id, driver, constructor, position_order, points, status):
        self.points = points
        self.positionOrder = position_order
        self.constructor = constructor
        self.driver = driver
        self.raceId = race_id
        self.resultId = result_id
        self.status = status


class ResultsReader(object):
    def __init__(self, path):
        self.path = path

    def parse_csv(self):
        csv = pandas.read_csv(self.path, ',', encoding="ISO-8859-1")
        # print(csv)
        races = []
        for index, row in csv.iterrows():
            races.append(Result(row['resultId'], row['raceId'], row['driverId'], row['constructorId']
                                , row['positionOrder'], row['points'], row['statusId']))
        return races
