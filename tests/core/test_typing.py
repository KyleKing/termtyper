import pytest

from tui_typer_tutor.core.typing import (
    ExpectedKey,
    Keys,
    TypedKey,
    _KeysAccum,
    get_adjusted_indices,
    on_keypress,
)


@pytest.mark.parametrize(('accum', 'start', 'end', 'expected_result'), [
    ([], 0, 10, (0, 0)),
    ([1, 2], 0, 1, (0, 1)),
    ([1, 2], 0, 2, (0, 2)),
    ([1, 2, 3, 4, 5], 0, 10, (0, 5)),
    ([1, 6, 11, 16], 0, 10, (0, 2)),
    ([1, 6, 11, 17], 6, 12, (1, 3)),
    ([1, 6, 11, 18], 5, 12, (0, 3)),
    ([1, 6, 11, 19], 7, 12, (1, 3)),
    ([1, 6, 11, 20], 7, 11, (1, 3)),
    ([1, 6, 11, 21], 7, 10, (1, 2)),
])
def test_get_indices(accum: list[int], start: int, end: int, expected_result: tuple[int, int]):
    result = [*get_adjusted_indices(accum, start, end)]  # act

    values = accum[result[0]:result[1]]
    assert tuple(result) == expected_result, f'{values} for {start}-{end} of {accum}'


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
        accum=_KeysAccum(expected=[], typed=[1]),
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
    assert keys.get_expected(2, 10) == keys.expected[1:]
    assert keys.get_expected(0, 1) == keys.expected[:1]
    assert keys.get_typed(2, 10) == keys.typed[1:]
    assert keys.get_typed(0, 1) == keys.typed[:1]
    assert_against_cache(keys)
