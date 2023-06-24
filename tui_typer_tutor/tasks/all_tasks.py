"""Configure CLI 'tasks'."""

from beartype import beartype
from invoke.context import Context
from invoke.tasks import task

from ..ui.tui import run


@task()
@beartype
def start(_ctx: Context) -> None:
    """Start Task."""
    run()
