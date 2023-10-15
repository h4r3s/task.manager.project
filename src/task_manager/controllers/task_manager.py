"""Task Manager controller module."""

import os
from datetime import datetime

from dotenv import load_dotenv

from .json_manager import JsonManager

load_dotenv()

JSON_FILE = os.getenv("JSON_FILE")


class TaskManager:
    def __init__(self, data_file):
        """
        Initialize an instance of TaskManager.

        Args:
            data_file (str): The path to the JSON file containing task data.

        Behavior:
            1. Attempts to read the JSON file to retrieve existing task data.
            2. If the file is found:
                - Sets the data file path (self.data_file).
                - Loads the existing data into self.data.
                - Determines the maximum task ID from the existing data (or sets it to 0 if no data exists).
            3. If the file is not found:
                - Prints an error message.
                - Initializes self.data as an empty list.

        Raises:
            FileNotFoundError: If the specified data_file is not found.
        """
        try:
            self.data_file = data_file
            self.data = JsonManager.read_json(data_file)
            self.max_id = (
                max(task["id"] for task in self.data) if self.data else 0
            )
        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            print(f"Error: File '{data_file}' not found.")
            self.data = []

    def list_all(self):
        """
        List all tasks.

        Behavior:
            Displays a formatted table with details of all tasks.
        """
        JsonManager.print_table(self.data)

    def find_by_id(self, id):
        """
        Find a task by its ID.

        Args:
            id (int): The ID of the task to be found.

        Behavior:
            1. Iterates through the list of tasks (self.data).
            2. If a task with the specified ID is found:
                - Print the details of the task in a formatted table.
                - Stop further iteration.
            3. If no task with the specified ID is found:
                - Print a message indicating that the task was not found.
        """
        for task in self.data:
            if task["id"] == id:
                JsonManager.print_table([task])
                break
        else:
            print(f"Task {id} not found")

    def create_task(self, title, description, due_date):
        """
        Create a new task with the provided details.

        Args:
            title (str): The title of the task.
            description (str): The description of the task.
            due_date (datetime.date): The due date of the task.

        Behavior:
            1. Checks if all required arguments (title, description, due_date) are provided.
            2. Verifies if the due date is today or later.
            3. If conditions are met:
                - Increments the max_id to generate a unique task ID.
                - Creates a new task with the specified details.
                - Appends the new task to the task list.
                - Writes the updated list back to the JSON file.
                - Prints a success message.
            4. If due date is earlier than today, prints an error message.

        Returns:
            None
        """
        if not title or not description or not due_date:
            print("Missing required arguments")
        else:
            today = datetime.today().date()
            if due_date.date() >= today:
                self.max_id += 1
                new_task = {
                    "id": self.max_id,
                    "title": title,
                    "description": description,
                    "dueDate": due_date.strftime("%Y-%m-%d"),
                    "status": "Pending",
                }
                self.data.append(new_task)
                JsonManager.write_json(JSON_FILE, self.data)
                print(f"Task {self.max_id} created successfully")
            else:
                print("Due date must be today or later")

    def update_task(
        self, id, title=None, description=None, due_date=None, status=None
    ):
        """
        Update an existing task with provided details.

        Args:
            id (int): The ID of the task to be updated.
            title (str, optional): The new title for the task. Defaults to None.
            description (str, optional): The new description for the task. Defaults to None.
            due_date (str, optional): The new due date for the task. Defaults to None.
            status (str, optional): The new status for the task. Defaults to None.

        Behavior:
            1. Iterates through the list of tasks (self.data).
            2. If a task with the specified ID is found:
                - If a new title is provided, update the task's title.
                - If a new description is provided, update the task's description.
                - If a new due date is provided, update the task's due date.
                - If a new status is provided, update the task's status.
                - Write the updated list back to the JSON file.
                - Print a success message.
                - Stop further iteration.
            3. If no task with the specified ID is found:
                - Print a message indicating that the task was not found.
            4. If the new due date is earlier than today:
                - Print a message indicating that the due date must be today or later.
        """
        for task in self.data:
            if task["id"] == id:
                if title:
                    task["title"] = title
                if description:
                    task["description"] = description
                if due_date:
                    today = datetime.today().date()
                    if due_date.date() >= today:
                        task["dueDate"] = due_date.strftime("%Y-%m-%d")
                    else:
                        print("Due date must be today or later")
                        return
                if status:
                    task["status"] = status
                JsonManager.write_json(JSON_FILE, self.data)
                print(f"Task {id} updated successfully")
                break
        else:
            print(f"Task {id} not found")

    def delete_task(self, id):
        """
        Deletes a task with the specified ID.

        Args:
            id (int): The ID of the task to be deleted.

        Returns:
            None

        Raises:
            None

        Behavior:
            1. Iterates through the list of tasks (self.data).
            2. If a task with the specified ID is found:
                - Removes the task from the list.
                - Writes the updated list back to the JSON file.
                - Prints a success message.
                - Stops further iteration.
            3. If no task with the specified ID is found:
                - Prints a message indicating that the task was not found.
        """
        for task in self.data:
            if task["id"] == id:
                self.data.remove(task)
                JsonManager.write_json(JSON_FILE, self.data)
                print(f"Task {id} deleted successfully")
                break
        else:
            print(f"Task {id} not found")
