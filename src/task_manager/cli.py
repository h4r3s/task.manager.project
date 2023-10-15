import os

import click
from controllers.task_manager import TaskManager
from dotenv import load_dotenv

load_dotenv()

JSON_FILE = os.getenv("JSON_FILE")


# Define the CLI application
@click.group()
def cli():
    pass


# Create an instance of TaskManager
task_manager = TaskManager(JSON_FILE)


# Define CLI commands
@cli.command()
def list_all():
    task_manager.list_all()


@cli.command()
@click.argument("id", type=int)
def find_by(id):
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
    task_manager.update_task(id, title, description, due_date, status)


@cli.command()
@click.argument("id", type=int)
def delete_task(id):
    task_manager.delete_task(id)


# Entry point for the CLI application
if __name__ == "__main__":
    cli()
