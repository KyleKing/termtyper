from tui_typer_tutor.core.seed_data import load_seed_data
from tui_typer_tutor.core.typing import ExpectedKey


def test_load_seed_data():
    result = load_seed_data('<Space>ld\n}')

    index = [idx for idx, _r in enumerate(result) if _r.raw == '}'][0]
    # Due to randomness, the index should either be first or last, but never internal
    result_removed = result.pop(0) if index == 0 else result.pop()
    assert result_removed == ExpectedKey(raw='}'), index
    assert result == [ExpectedKey(raw='<Space>'), ExpectedKey(raw='l'), ExpectedKey(raw='d')]
