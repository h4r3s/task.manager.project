from click.testing import CliRunner

from ..task_manager.cli import cli

runner = CliRunner()


def test_list_all():
    result = runner.invoke(cli, ["list_all"])
    assert result.exit_code == 0


def test_find_by():
    result = runner.invoke(cli, ["find_by", "1"])
    assert result.exit_code == 0


def test_create_task():
    result = runner.invoke(
        cli,
        [
            "create_task",
            "--title",
            "Test Task",
            "--description",
            "Test Description",
            "--due-date",
            "2023-10-15",
        ],
    )
    assert result.exit_code == 0
