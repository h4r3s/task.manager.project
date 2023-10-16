"""CLI module.

This module defines a command-line interface (CLI) for interacting with a task manager application.
It leverages the `click` library for creating commands and handling command-line arguments.
"""

import os

import click
from controllers.task_manager import TaskManager
from dotenv import load_dotenv

load_dotenv()

JSON_FILE = os.getenv("JSON_FILE")


# Define the CLI application
@click.group()
def cli():
    """
    Entry point for the CLI application.

    This function serves as the entry point for the CLI application. It does not take any arguments.
    """
    pass


# Create an instance of TaskManager
task_manager = TaskManager(JSON_FILE)


# Define CLI commands
@cli.command()
def list_all():
    """
    List all tasks.

    This command lists all tasks currently stored in the JSON file.
    """
    task_manager.list_all()


@cli.command()
@click.argument("id", type=int)
def find_by(id):
    """
    Find a task by its ID.

    Args:
        id (int): The unique ID of the task.
    """
    task_manager.find_by_id(id)


@cli.command()
@click.option("--title", required=True, help="Title of the task")
@click.option("--description", required=True, help="Description of the task")
@click.option(
    "--due-date",
    required=True,
    type=click.DateTime(formats=["%Y-%m-%d"]),
    help="Due date of the task (YYYY-MM-DD)",
)
def create_task(title, description, due_date):
    """
    Create a new task.

    Args:
        title (str): Title of the task.
        description (str): Description of the task.
        due_date (str): Due date of the task in the format YYYY-MM-DD.
    """
    task_manager.create_task(title, description, due_date)


@cli.command()
@click.argument("id", type=int)
@click.option("--title", help="Title of the task")
@click.option("--description", help="Description of the task")
@click.option(
    "--due-date",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    help="Due date of the task (YYYY-MM-DD)",
)
@click.option(
    "--status",
    type=click.Choice(["Pending", "Executing", "Completed"]),
    help="Status of the task",
)
def update_task(id, title, description, due_date, status):
    """
    Update an existing task.

    Args:
        id (int): The unique ID of the task.
        title (str): Updated title of the task (optional).
        description (str): Updated description of the task (optional).
        due_date (str): Updated due date of the task in the format YYYY-MM-DD (optional).
        status (str): Updated status of the task (optional).
    """
    task_manager.update_task(id, title, description, due_date, status)


@cli.command()
@click.argument("id", type=int)
def delete_task(id):
    """
    Delete a task by its ID.

    Args:
        id (int): The unique ID of the task to be deleted.
    """
    task_manager.delete_task(id)


# Entry point for the CLI application
if __name__ == "__main__":
    cli()
