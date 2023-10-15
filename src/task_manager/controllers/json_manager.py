import json
import os

from dotenv import load_dotenv
from prettytable import PrettyTable

load_dotenv()

JSON_FILE = os.getenv("JSON_FILE")


class JsonManager:
    def read_json(file_name):
        """
        Reads a JSON file and returns a list of dictionaries.

        Args:
            file_name (str): The name of the JSON file.

        Returns:
            list: A list of dictionaries representing the data from the JSON file.
        """
        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                json.dump([], f)
        with open(file_name, "r") as f:
            data = json.load(f)
        return data

    def write_json(file_name, data):
        """
        Writes a list of dictionaries to a JSON file.

        Args:
            file_name (str): The name of the JSON file.
            data (list): A list of dictionaries to be written to the file.
        """
        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)

    def print_table(data):
        """
        Prints tasks in a formatted table.

        Args:
            data (list): A list of task dictionaries.
        """
        table = PrettyTable()
        table.field_names = [
            "Task ID",
            "Title",
            "Description",
            "Due Date",
            "Status",
        ]

        for task in data:
            table.add_row(
                [
                    task["id"],
                    task["title"],
                    task["description"],
                    task["dueDate"],
                    task["status"],
                ]
            )

        print(table)
