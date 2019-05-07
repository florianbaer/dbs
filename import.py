from circuit_reader import CircuitsReader
from constructor_reader import ConstructorReader
from driver_reader import DriverReader
from races_reader import RacesReader
from results_reader import ResultsReader
from pyravendb.store import document_store

from status_reader import StatusReader


def read_driver():
    path = "data/drivers.csv"
    driver_reader = DriverReader(path)
    driver_reader.parse_csv()
    return driver_reader

def read_races(circuit_reader):
    path = "data/races.csv"
    races_reader = RacesReader(path, circuit_reader)
    return races_reader.parse_csv()

def read_circuits():
    path = "data/circuits.csv"
    circuits_reader = CircuitsReader(path)
    circuits_reader.parse_csv()
    return circuits_reader

def read_status():
    path = "data/status.csv"
    status_reader = StatusReader(path)
    status_reader.parse_csv()
    return status_reader

def read_constructor():
    path = "data/constructors.csv"
    constructor_reader = ConstructorReader(path)
    constructor_reader.parse_csv()
    return constructor_reader


def read_results(driver_reader, constructor_reader, status_reader):
    path = "data/results.csv"
    results_reader = ResultsReader(path, driver_reader, constructor_reader, status_reader)
    return results_reader.parse_csv()



def main():
    store = document_store.DocumentStore(urls=["http://localhost:8080"], database="RacerAnalysis")
    store.initialize()


    circuits_reader = read_circuits()
    races_reader = read_races(circuits_reader)

    for datastore_result in races_reader:
        with store.open_session() as session:
            session.store(datastore_result)
            session.save_changes()


    driver_reader = read_driver()
    constructor_reader = read_constructor()
    status_reader = read_status()
    results = read_results(driver_reader, constructor_reader, status_reader)


    for datastore_result in results:
        with store.open_session() as session:
            session.store(datastore_result)
            session.save_changes()

if __name__ == "__main__":
    main()
