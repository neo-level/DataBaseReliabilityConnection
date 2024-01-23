from DataManager import DataManager
from mssql_logger import MSSQLLogger
from database_connector import DatabaseConnector
from database import Database


def main():
    data_manager = DataManager()
    db_info = data_manager.get_database_information()
    db_connector = DatabaseConnector(server=db_info["server"], database=db_info["database"],
                                     username=db_info["username"], password=db_info["password"])
    db = Database(connector=db_connector)
    logger = MSSQLLogger(database=db, interval=60)
    logger.log_timestamp()


if __name__ == "__main__":
    main()
