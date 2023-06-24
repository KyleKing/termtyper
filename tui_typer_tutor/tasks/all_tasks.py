"""Configure CLI 'tasks'."""

from beartype import beartype
from invoke.context import Context
from invoke.tasks import task


@task()
@beartype
def start(_ctx: Context) -> None:
    """Start Task."""
    # FIXME: Accept paths to:
    # - JSON files with "command name": "character sequence" pairs
    # - or a text file with token per line
    # TODO: Use a bidict to convert from vim to textual key binds (i.e. `that = bidict({"<c-a>": "ctrl+a"})`, then `that['<c-a>']` and `that.inverse['ctrl+a']`)
    # TODO: Export from AstronVim the keybindings:
    #   https://github.com/AstroNvim/AstroNvim/blob/377db3f7d6273779533c988dadc07a08e0e43f2e/lua/astronvim/mappings.lua
    from ..app.typer import run

    run()


@task()
@beartype
def keys(_ctx: Context) -> None:
    """Keys Task."""
    from ..keys import run

    run()


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
