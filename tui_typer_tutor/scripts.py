"""Start the command line program."""

import argparse
import sys

from beartype import beartype

from . import __version__
from .app.ttt import TuiTyperTutor


@beartype
def start() -> None:  # pragma: no cover
    """CLI Entrypoint."""
    parser = argparse.ArgumentParser(description='Practice Touch Typing')
    parser.add_argument(
        '-v', '--version', action='version',
        version=f'%(prog)s {__version__}', help="Show program's version number and exit.",
    )
    parser.parse_args(sys.argv[1:])

    TuiTyperTutor().run()
