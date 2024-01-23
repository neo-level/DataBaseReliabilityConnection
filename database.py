class Database:
    def __init__(self, connector):
        self.connector = connector

    def create_table(self, table_name, columns):
        """
        Create a new table in the database.
        """

        cursor = self.connector.cursor()
        cursor.execute(f"SELECT name FROM sys.tables WHERE name = '{table_name}'")
        if cursor.fetchone():
            print(f"Table '{table_name}' already exists.")
            return

        columns_str = ', '.join([f'{name} {data_type}' for name, data_type in columns.items()])
        query = f"CREATE TABLE {table_name} ({columns_str})"
        try:
            cursor.execute(query)
            self.connector.commit()
        except Exception as e:
            print(f"Failed to create table. Error: {e}")

    def insert(self, table, columns, values):
        """
        Inserts a row into the specified table with the given columns and values.
        """

        columns_string = ', '.join(columns)
        values_string = ', '.join(['?'] * len(values))
        query = f'INSERT INTO {table} ({columns_string}) VALUES ({values_string})'
        cursor = self.connector.cursor()
        try:
            cursor.execute(query, values)
            self.connector.commit()
        except Exception as e:
            print("Failed to execute insert operation: ", e)

    def update(self, table, set_column, set_value, condition_column, condition_value):
        """
        Update method to update a record in a table based on a given condition.
        """

        query = f'UPDATE {table} SET {set_column} = ? WHERE {condition_column} = ?'
        cursor = self.connector.cursor()
        try:
            cursor.execute(query, (set_value, condition_value))
            self.connector.commit()
        except Exception as e:
            print("Failed to execute update operation: ", e)

    def select(self, table, columns, condition_column=None, condition_value=None):
        """
        Selects data from a table based on the specified conditions.
        """

        columns_string = ', '.join(columns)
        query = f'SELECT {columns_string} FROM {table}'
        if condition_column and condition_value:
            query += f' WHERE {condition_column} = ?'
        cursor = self.connector.cursor()
        try:
            cursor.execute(query, (condition_value,))
            return cursor.fetchall()
        except Exception as e:
            print("Failed to execute select operation: ", e)
