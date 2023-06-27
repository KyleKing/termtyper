"""Seed data for tests."""

from tui_typer_tutor.core.typing import ExpectedKey, Keys, TypedKey


def lol_keys() -> Keys:
    """Expected 'lol' with only 'l' typed initially."""
    return Keys(
        expected=[
            ExpectedKey(textual='l'),
            ExpectedKey(textual='o'),
            ExpectedKey(textual='l'),
        ],
        typed_all=[
            TypedKey(textual='l', expected=ExpectedKey(textual='l')),
        ],
        typed=[
            TypedKey(textual='l', expected=ExpectedKey(textual='l')),
        ],
        last_was_delete=False,
    )
