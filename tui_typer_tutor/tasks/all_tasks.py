"""Configure CLI 'tasks'."""

from beartype import beartype
from invoke.context import Context
from invoke.tasks import task

# FIXME: This should probably just be like tail-jsonl without tasks


@task()
@beartype
def start(_ctx: Context) -> None:
    """Start Task."""
    raise NotImplementedError


@task()
@beartype
def termtyper(_ctx: Context) -> None:
    """`termtyper` Task.

    Requires downgrading to textual `0.1`

    Will see errors like:

    ```
    AttributeError: 'TermTyper' object has no attribute 'view'
    ```

    """
    from ..ui.tui import run

    run()
