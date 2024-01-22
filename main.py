from DataManager import DataManager
from mssql_logger import MSSQLLogger


def main():
    data_manager = DataManager()
    db_info = data_manager.get_database_information()
    logger = MSSQLLogger(server=db_info["server"], database=db_info["database"],
                         username=db_info["username"], password=db_info["password"])
    logger.connect()
    logger.create_table()
    logger.log_timestamp()


if __name__ == "__main__":
    main()
