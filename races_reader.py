import pandas


class Race(object):
    def __init__(self, Id, raceId, name, year,  circuit):
        self.name = name
        self.year = year
        self.circuit = circuit
        self.Id = Id
        self.raceId = raceId

class RacesReader(object):
    def __init__(self, path, circuit_reader):
        self.circuit_reader = circuit_reader
        self.path = path

    def parse_csv(self):
        self.csv = pandas.read_csv(self.path, ',', encoding="ISO-8859-1")
        # self.csv.set_index('raceId', inplace=True)
        races = []
        for index, row in self.csv.iterrows():
            races.append(Race("race/" + str(row['raceId']),
                                    row['raceId'],
                                    row['name'],
                                    row['year'],
                                    self.circuit_reader.get_circuit(row['circuitId'])))
        return races

    def get_name_by_id(self, raceId):
        row = self.csv.loc[[raceId], :]
        return row['name'].values[0]

