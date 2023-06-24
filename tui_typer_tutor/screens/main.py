"""The main screen for the application."""

import math
from os import get_terminal_size
from string import ascii_lowercase, digits, punctuation
from typing import ClassVar

from textual import on
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.events import Key
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label, Static

from ..constants import VIM_TO_TEXTUAL

TERM_X, _TERM_Y = get_terminal_size()
MAX_CHARS = math.floor(0.80 * TERM_X)


class Main(Screen[None]):  # pylint:disable=too-many-public-methods
    """The main screen for the application."""

    DEFAULT_CSS: ClassVar[str] = """
    Screen {
        background: #1b2b34;
    }

    #left-pad {
        width: 10%;
    }
    #content {
        width: 80%;
        align: center middle;
    }

    .tutor-container {
        content-align-horizontal: left;
        height: 3;
    }
    #text {
        color: #7e8993;
    }
    #typed-container .error {
        color: #ec5f67;
    }
    #typed-container .warning {
        color: #fac863;
    }
    #typed-container .success {
        color: #99c794;
    }
    """

    typed_text: str = ''
    # FIXME: I need a display key b/c some VIM keys are multiple letters
    display_text: str = 'start!' + (ascii_lowercase + punctuation + digits)
    is_testing: bool = False

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Vertical(id='left-pad')
            # HACK: ^^ couldn't get 'center' alignment to work
            with Vertical(id='content'):
                # PLANNED: Add a horizontal scrollbar above the content
                with Horizontal(id='text-container', classes='tutor-container'):
                    yield Label('', id='text')
                yield Horizontal(id='typed-container', classes='tutor-container')
                # TODO: Show the 'command name' somewhere
                # TODO: Show commands as separated groups that don't need a delimiter
                yield Button('Loading...', id='focus-toggle')
                yield Static('If using WezTerm, adjust font size with <C-> and <C+>, reset with <C0>')
        yield Footer()

    @on(Button.Pressed, '#focus-toggle')
    def _toggle_focus(self) -> None:
        toggle = self.query_one('#focus-toggle', Button)
        self.is_testing = not self.is_testing
        if self.is_testing:
            toggle.label = 'Pause'
            toggle.variant = 'error'
        else:
            toggle.label = 'Resume'
            toggle.variant = 'success'

    def on_mount(self) -> None:
        self.query_one('#text', Label).update(self.display_text[:MAX_CHARS])
        self._toggle_focus()

    def on_key(self, event: Key) -> None:
        """Capture all key presses and show in the typed input."""
        # TODO: emit events of: typed key, expected key, index for tracking
        if not self.is_testing:
            return

        if event.key == 'backspace':
            if self.typed_text:
                self.typed_text = self.typed_text[:-1]
                self.query('Label.typed').last().remove()
        else:
            key = VIM_TO_TEXTUAL.inverse.get(event.key) or event.key
            self.typed_text += key
            count = len(self.typed_text)
            color_class = 'warning'
            if count <= len(self.display_text):
                was_correct = key == self.display_text[count - 1]
                color_class = 'success' if was_correct else 'error'
            next_label = Label(key, classes=f'typed {color_class}')
            if count >= MAX_CHARS:
                self.query('Label.typed').first().remove()
            self.query_one('#typed-container', Horizontal).mount(next_label)

        start = max(len(self.typed_text) - MAX_CHARS, 0)
        self.query_one('#text', Label).update(self.display_text[start:][:MAX_CHARS])
