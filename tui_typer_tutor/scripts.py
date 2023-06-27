"""Start the command line program."""

import argparse
import sys

from beartype import beartype

from . import __version__
from .app.ttt import TuiTyperTutor
from .core.uninstall import uninstall


@beartype
def start() -> None:  # pragma: no cover
    """CLI Entrypoint."""
    parser = argparse.ArgumentParser(description='Practice Touch Typing')
    parser.add_argument(
        '-v', '--version', action='version',
        version=f'%(prog)s {__version__}', help="Show program's version number and exit.",
    )
    parser.add_argument(
        '--uninstall', action='store_true', help='Remove all files created by tui-typer-tutor.',
    )
    args = parser.parse_args(sys.argv[1:])

    if args.uninstall:
        uninstall()
    else:
        TuiTyperTutor().run()
