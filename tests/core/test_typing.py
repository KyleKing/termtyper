import pytest

from tui_typer_tutor.core.typing import (
    ExpectedKey,
    Keys,
    TypedKey,
    on_keypress,
)


def _lol_text() -> Keys:
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


@pytest.mark.parametrize(
    ('raws', 'keys'),
    [
        (['ctrl+q'], Keys(expected=[ExpectedKey(textual='s')])),
        (['t'], _lol_text()),
        (['backspace'], _lol_text()),
        (['backspace', 'backspace', 'l', 'o', 'l'], _lol_text()),
    ],
)
def test_on_keypress(
    raws: str,
    keys: Keys,
    assert_against_cache,
):
    for raw in raws:
        on_keypress(raw, keys)  # act

    assert_against_cache(keys)


@pytest.mark.parametrize(
    ('raw', 'was_correct'),
    [
        ('0', False),
        ('o', True),
    ],
)
def test_on_keypress___extended(
    *,
    raw: str,
    was_correct: bool,
    assert_against_cache,
):
    keys = _lol_text()

    on_keypress(raw, keys)  # act

    assert keys.typed[-1].was_correct == was_correct
    assert_against_cache(keys)
