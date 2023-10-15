"""Task Manager tests."""

from datetime import datetime, timedelta

import pytest

from src.task_manager.controllers.task_manager import TaskManager


class MockJsonManager:
    def read_json(self):
        return [
            {
                "id": 1,
                "title": "Task 1",
                "description": "Description 1",
                "dueDate": "2023-10-15",
                "status": "Pending",
            },
            {
                "id": 2,
                "title": "Task 2",
                "description": "Description 2",
                "dueDate": "2023-10-16",
                "status": "Completed",
            },
        ]

    def write_json(self, filename, data):
        pass


def test_list_all(capsys):
    task_manager = TaskManager(MockJsonManager())
    task_manager.list_all()
    captured = capsys.readouterr()
    assert "Task 1" in captured.out
    assert "Task 2" in captured.out


def test_find_by_id(capsys):
    task_manager = TaskManager(MockJsonManager())
    task_manager.find_by_id(1)
    captured = capsys.readouterr()
    assert "Task 1" in captured.out


def test_find_by_id_not_found(capsys):
    task_manager = TaskManager(MockJsonManager())
    task_manager.find_by_id(3)
    captured = capsys.readouterr()
    assert "Task 3 not found" in captured.out


def test_create_task_with_valid_params(capsys):
    task_manager = TaskManager(MockJsonManager())
    task_manager.create_task(
        "Task 3", "Description 3", datetime.now() + timedelta(days=1)
    )
    captured = capsys.readouterr()
    assert "Task created successfully" in captured.out


def test_create_task_with_invalid_due_date(capsys):
    task_manager = TaskManager(MockJsonManager())
    task_manager.create_task(
        "Task 3", "Description 3", datetime.now() - timedelta(days=1)
    )
    captured = capsys.readouterr()
    assert "Due date must be today or later" in captured.out


def test_update_task_with_valid_params(capsys):
    task_manager = TaskManager(MockJsonManager())
    task_manager.update_task(1, title="Task 1 Updated")
    captured = capsys.readouterr()
    assert "Task 1 updated successfully" in captured.out


def test_update_task_with_invalid_due_date(capsys):
    task_manager = TaskManager(MockJsonManager())
    task_manager.update_task(1, due_date=datetime.now() - timedelta(days=1))
    captured = capsys.readouterr()
    assert "Due date must be today or later" in captured.out


def test_update_task_not_found(capsys):
    task_manager = TaskManager(MockJsonManager())
    task_manager.update_task(3, title="Task 3 Updated")
    captured = capsys.readouterr()
    assert "Task 3 not found" in captured.out


def test_delete_task_with_valid_id(capsys):
    task_manager = TaskManager(MockJsonManager())
    task_manager.delete_task(1)
    captured = capsys.readouterr()
    assert "Task 1 deleted successfully" in captured.out


def test_delete_task_not_found(capsys):
    task_manager = TaskManager(MockJsonManager())
    task_manager.delete_task(3)
    captured = capsys.readouterr()
    assert "Task 3 not found" in captured.out
