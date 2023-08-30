from pathlib import Path

import arrow
import pandas as pd
import platformdirs
import pytest
from freezegun import freeze_time

from tui_typer_tutor import APP_NAME
from tui_typer_tutor.core.metrics import SessionMetrics, append_csv
from tui_typer_tutor.core.typing import on_keypress

from ..configuration import FROZEN_TIME, stubbed_user_cache_dir
from ..seed_data import lol_keys


@pytest.mark.parametrize('iterations', [1, 2])
def test_append_csv(
    iterations: int,
    snapshot,
    monkeypatch,
    fix_test_cache,  # noqa: ARG001
):
    monkeypatch.setattr(platformdirs, 'user_cache_dir', stubbed_user_cache_dir)
    csv_path = Path(stubbed_user_cache_dir(APP_NAME)) / 'metrics.csv'
    keys = lol_keys()

    all_metrics = []
    frozen_time = FROZEN_TIME
    for idx in range(1, iterations + 1):
        with freeze_time(frozen_time):
            metrics = SessionMetrics.from_filename(filename='seed_file')

        frozen_time = arrow.get(frozen_time).shift(minutes=idx).datetime
        with freeze_time(frozen_time):
            append_csv(metrics.end_session(keys))  # act
        all_metrics.append(metrics)
        on_keypress(str(idx), keys)

    df_csv = pd.read_csv(csv_path)
    assert {
        'metrics': all_metrics[-1].dict(),
        'csv': df_csv.to_dict(orient='list'),
    } == snapshot
