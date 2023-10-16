# Task Manager CLI

A simple command-line interface (CLI) application for managing tasks.

For this project, we are utilizing Python as our programming language. We have integrated the Click library to facilitate Command Line Interface (CLI) interactions. Additionally, we are adopting a modular programming approach to enhance code organization and maintainability

In our approach, we've segmented the code into distinct layers. One layer is responsible for handling JSON data, another for managing tasks, and a third for creating commands for the command-line interface (CLI). Additionally, we've incorporated an environment file to enhance code flexibility and maintainability.

Keeping in mind the principle of "keeping it simple",

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Available Commands](#available-commands)
  - [Usage Examples](#usage-examples)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/h4r3s/task.manager.project.git
cd Task.manager
```

2. Create a virtual environment and activate it:

```bash

python3.8 -m venv var/venv
source var/venv/bin/activate
python3.8 -m pip install --upgrade pip
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Navigate to the `src/task_manager/` directory and run the CLI application:

```bash
python cli.py [options] [command]
```

### Available Commands

- `list_all`: List all tasks.
- `find_by [id]`: Find a task by its ID.
- `create_task --title [title] --description [description] --due-date [due_date]`: Create a new task.
- `update_task [id] [--title] [--description] [--due-date] [--status]`: Update an existing task.
- `delete_task [id]`: Delete a task.

#### Usage Examples

List all tasks:

```bash
python cli.py list_all
```

Find a task by its ID:

```bash
python cli.py find_by 1
```

Create a new task:

```bash
python cli.py create_task --title "Task 1" --description "This is task 1" --due-date "2021-01-01"
```

Update an existing task:

```bash
python cli.py update_task 1 --title "Task 1" --description "This is task 1" --due-date "2021-01-01" --status "Completed"
```

Delete a task:

```bash
python cli.py delete_task 1
```

## Author

[Jorge Jimenez]

## Project Structure

- `src/`: Contains the source code for the application.
  - `task_manager/`: Main module for the Task Manager application.
    - `cli.py`: Entry point for the CLI application.
    - `.env`: Environment configuration file (if any).
    - `__init__.py`: Initialization file.
    - `resources/`: Contains data files.
      - `data.json`: Store for task data.
    - `controllers/`: Controllers for managing tasks.
      - `__init__.py`: Initialization file.
      - `task_manager.py`: Task management logic.
      - `json_manager.py`: JSON file handling.
- `tests/`: Contains test cases.
  - `__init__.py`: Initialization file.
  - `test_cli.py`: Tests for the CLI functionality.
  - `test_task_controller.py`: Tests for the task controller.
- `var/`: Directory for storing variable data (logs, cache, etc.).
- `README.md`: This file.
- `requirements.txt`: List of dependencies for the project.

## Testing

To run the tests, use the following command:

**Advice:** TESTS ARE NOT AVALIABLE YET -- WIP

**Advice:** Patience is key; progress takes time and effort. Keep going!

```bash
pytest tests/
```

## Contributing

If you'd like to contribute, please fork the repository and create a pull request.

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.
