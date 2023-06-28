from pathlib import Path

import platformdirs

from tui_typer_tutor import APP_NAME
from tui_typer_tutor.core.uninstall import uninstall

from ..configuration import stubbed_user_cache_dir


def test_uninstall(monkeypatch):
    monkeypatch.setattr(platformdirs, 'user_cache_dir', stubbed_user_cache_dir)
    csv_path = Path(stubbed_user_cache_dir(APP_NAME)) / 'metrics.csv'
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.write_text('')

    uninstall()

    assert not csv_path.parent.is_dir()
