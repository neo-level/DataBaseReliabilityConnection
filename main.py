import os
from mssql_logger import MSSQLLogger

server = os.getenv("MSSQL_SERVER")
database = os.getenv("MSSQL_DB")
user = os.getenv("MSSQL_USER")
password = os.getenv("MSSQL_PASSWORD")

logger = MSSQLLogger(server=server, database=database, username=user, password=password)

logger.connect()
logger.create_table()
logger.log_timestamp()
