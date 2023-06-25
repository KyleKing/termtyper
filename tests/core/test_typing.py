import pytest

from tui_typer_tutor.core.typing import (
    ExpectedKey,
    Keys,
    TypedKey,
    _KeysAccum,
    on_keypress,
)


def _lol_text() -> Keys:
    """Expected 'lol' with only 'l' typed initially."""
    return Keys(
        expected=[
            ExpectedKey(raw='l'),
            ExpectedKey(raw='o'),
            ExpectedKey(raw='l'),
        ],
        typed_all=[
            TypedKey(raw='l', expected=ExpectedKey(raw='l')),
        ],
        typed=[
            TypedKey(raw='l', expected=ExpectedKey(raw='l')),
        ],
        last_was_delete=False,
        accum=_KeysAccum(expected=[], typed=[1]),
    )


@pytest.mark.parametrize(
    ('raws', 'keys'),
    [
        (['ctrl+q'], Keys(expected=[ExpectedKey(raw='s')])),
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
        on_keypress(raw, keys)

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
    on_keypress(raw, keys)

    assert keys.typed[-1].was_correct == was_correct
    assert keys.get_expected(1, 10) == keys.expected[1:]
    assert keys.get_expected(0, 1) == keys.expected[:1]
    assert keys.get_typed(1, 10) == keys.typed[1:]
    assert keys.get_typed(0, 1) == keys.typed[:1]
    assert_against_cache(keys)
