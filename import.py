from racer_reader import RacerReader
from races_reader import RacesReader
from results_reader import ResultsReader


def read_racer():
    path = "data/drivers.csv"
    racer_reader = RacerReader(path)
    racer_reader.parse_csv()

def read_races():
    path = "data/races.csv"
    races_reader = RacesReader(path)
    races_reader.parse_csv()

def read_results():
    path = "data/results.csv"
    races_reader = ResultsReader(path)
    races_reader.parse_csv()


def main():
    # races = read_races()
    read_results()




if __name__ == "__main__":
    main()
