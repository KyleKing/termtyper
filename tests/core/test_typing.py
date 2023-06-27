import pytest

from tui_typer_tutor.core.typing import (
    ExpectedKey,
    Keys,
    on_keypress,
)

from ..seed_data import lol_keys


@pytest.mark.parametrize(
    ('raws', 'keys'),
    [
        (['ctrl+q'], Keys(expected=[ExpectedKey(textual='s')])),
        (['t'], lol_keys()),
        (['backspace'], lol_keys()),
        (['backspace', 'backspace', 'l', 'o', 'l'], lol_keys()),
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
    keys = lol_keys()

    on_keypress(raw, keys)  # act

    assert keys.typed[-1].was_correct == was_correct
    assert_against_cache(keys)
