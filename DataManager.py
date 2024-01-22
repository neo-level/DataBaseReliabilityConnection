import json
import sys


class DataManager:
    """
    DataManager class that provides methods for retrieving database information.
    """

    def get_database_information(self):
        """
        Retrieve database information from a JSON file.

        :return: A dictionary containing the database information.
        """
        try:
            with open("databaseInformation.json") as json_file:
                config = json.load(json_file)
            json_file.close()
        except FileNotFoundError:
            print("No database information file found.")
            self.generate_empty_database_info()
            sys.exit()

        return config

    def generate_empty_database_info(self):

        """
        This function generates an empty database information template.
        """
        database_info = {"server": "", "database": "", "username": "", "password": ""}

        with open("databaseInformation.json", "w") as json_file:
            json.dump(database_info, json_file, indent=4)

        print("Template for database information is being generated. Please fill in the details.")
