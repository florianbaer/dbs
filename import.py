from constructor_reader import ConstructorReader
from driver_reader import DriverReader
from races_reader import RacesReader
from results_reader import ResultsReader
from pyravendb.store import document_store


def read_driver():
    path = "data/drivers.csv"
    driver_reader = DriverReader(path)
    driver_reader.parse_csv()
    return driver_reader

def read_races():
    path = "data/races.csv"
    races_reader = RacesReader(path)
    races_reader.parse_csv()
    return races_reader

def read_constructor():
    path = "data/constructors.csv"
    constructor_reader = ConstructorReader(path)
    constructor_reader.parse_csv()
    return constructor_reader


def read_results(driver_reader, constructor_reader):
    path = "data/results.csv"
    races_reader = ResultsReader(path, driver_reader, constructor_reader)
    return races_reader.parse_csv()



def main():
    store = document_store.DocumentStore(urls=["http://localhost:8080"], database="RacerAnalysis")
    store.initialize()

    driver_reader = read_driver()
    constructor_reader = read_constructor()
    results = read_results(driver_reader, constructor_reader)


    with store.open_session() as session:
        for datastore_result in results:
            session.store(datastore_result.race_result)
            print(datastore_result.race_result.raceId)
            print(datastore_result.race_result.resultId)
            print(datastore_result.race_result.status)
            print(datastore_result.race_result.positionOrder)
            print(datastore_result.race_result.points)
            session.save_changes()
            session.store(datastore_result.driver)
            print(datastore_result.driver.driver_id)
            print(datastore_result.driver.forename)
            print(datastore_result.driver.surname)
            print(datastore_result.driver.nationality)
            session.save_changes()
            session.store(datastore_result.constructor)
            print(datastore_result.constructor)
            print(datastore_result.constructor.constructor_id)
            print(datastore_result.constructor.name)
            print(datastore_result.constructor.constructor_id)
            session.save_changes()

    races_reader = read_races()


if __name__ == "__main__":
    main()
