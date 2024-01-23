import pyodbc


class DatabaseConnector:
    """
    DatabaseConnector is a class that allows connecting to a SQL Server database using the specified connection string.
    """

    def __init__(self, server, database, username, password):
        self.cursor = None
        self.connection = None
        self.connection_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt={True};TrustServerCertificate={True}'

    def connect(self):
        """
        Connects to the database using the specified connection string.
        """

        try:
            self.connection = pyodbc.connect(self.connection_str)
            self.cursor = self.connection.cursor()
            print("Database connection successful.")
        except pyodbc.Error as e:
            print("Database connection error: ", e)
