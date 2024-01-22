import pyodbc
import time
from datetime import datetime


class MSSQLLogger:
    """
    Class for logging timestamps to a Microsoft SQL Server database.

    :param server: The server name or IP address.
    :type server: str
    :param database: The name of the database.
    :type database: str
    :param username: The username used for authentication.
    :type username: str
    :param password: The password used for authentication.
    :type password: str
    """

    def __init__(self, server, database, username, password):
        self.cursor = None
        self.connection = None
        self.connection_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt={True};TrustServerCertificate={True}'
        self.INTERVAL = 60  # interval in seconds for logging timestamp

    def connect(self):
        """
        Connects to the database using the specified connection string.

        :return: None
        """
        try:
            self.connection = pyodbc.connect(self.connection_str)
            self.cursor = self.connection.cursor()
            print("Database connection successful.")
        except pyodbc.Error as e:
            print("Database connection error: ", e)

    def create_table(self):
        """
        Create a table named 'timestamps' if it does not already exist.

        :return: None
        """
        self.cursor.execute('''
            IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'timestamps' AND type = 'U') 
            BEGIN 
                CREATE TABLE timestamps ( 
                    timestamp datetime 
                ) 
            END
        ''')
        self.connection.commit()
        print("'timestamps' table is ready for use.")

    def log_timestamp(self):
        """
        Logs current timestamp to the database at regular intervals.

        :return: None
        """
        while True:
            try:
                timestamp = datetime.now()
                timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                self.cursor.execute(f"INSERT INTO timestamps (timestamp) VALUES ('{timestamp}')")
                self.connection.commit()
                print(f"Timestamp {timestamp} has been logged to the database.")
            except pyodbc.Error as e:
                print("Error while logging timestamp: ", e)
            time.sleep(self.INTERVAL)
