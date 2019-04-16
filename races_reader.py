import pandas


class Race(object):
    def __init__(self, Id, name, year,  circuit):
        self.name = name
        self.year = year
        self.circuit = circuit
        self.Id = Id

class RacesReader(object):
    def __init__(self, path, circuit_reader):
        self.circuit_reader = circuit_reader
        self.path = path

    def parse_csv(self):
        self.csv = pandas.read_csv(self.path, ',', encoding="ISO-8859-1")
        races = []
        for index, row in self.csv.iterrows():
            races.append(Race("race/" + str(row['raceId']),
                                    row['name'],
                                    row['year'],
                                    self.circuit_reader.get_circuit(row['circuitId'])))
        return races
