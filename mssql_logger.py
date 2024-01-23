import pyodbc
import time
from datetime import datetime


class MSSQLLogger:
    """
    This class is used to log timestamps to a Microsoft SQL Server database at regular intervals.
    """

    def __init__(self, database, interval):
        self.interval = interval
        self.database = database
        database.create_table('timestamps', {"timestamp": "datetime"})

    def get_timestamp(self):
        """
        Returns the current timestamp in the format "YYYY-MM-DD HH:MM:SS".
        """

        timestamp = datetime.now()
        return timestamp.strftime("%Y-%m-%d %H:%M:%S")

    def log_timestamp(self):
        """
        Logs current timestamp to the database at regular intervals.

        :return: None
        """
        while True:
            try:
                self.database.insert('timestamps', {"timestamp": self.get_timestamp()})
                print(f"Timestamp {self.get_timestamp()} has been logged to the database.")
            except pyodbc.Error as e:
                print("Error while logging timestamp: ", e)
            time.sleep(self.interval)
