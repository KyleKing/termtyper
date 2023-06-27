"""Manage Metrics."""

import csv
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from beartype import beartype
from pydantic import BaseModel

from .typing import Keys


@beartype
def utcnow() -> datetime:
    """Return the current time in UTC."""
    return datetime.now(tz=ZoneInfo('UTC'))


class SessionMetrics(BaseModel):
    """Session metrics."""

    filename: str
    session_start: datetime
    session_end: datetime | None = None
    typed_correct: int = 0
    typed_incorrect: int = 0

    @classmethod
    def from_filename(cls, filename: str) -> 'SessionMetrics':  # noqa: RBT002
        """Initialize Metrics based on the filename."""
        return cls(filename=filename, session_start=utcnow())

    def end_session(self, keys: Keys) -> 'SessionMetrics':  # noqa: RBT002
        """Update the typed counters based on `Keys`."""
        self.session_end = utcnow()
        for key in keys.typed_all:
            if key.expected:
                if key.was_correct:
                    self.typed_correct += 1
                else:
                    self.typed_incorrect += 1
        return self


# PLANNED: Support Linux/Windows
CSV_PATH = Path.home() / '.config/tui-typer-tutor/metrics.csv'


@beartype
def append_csv(metrics: SessionMetrics) -> None:
    """Write metrics to the global CSV."""
    csv_columns = ['filename', 'session_start', 'session_end', 'typed_correct', 'typed_incorrect']
    if not CSV_PATH.is_file():
        CSV_PATH.parent.mkdir(exist_ok=True, parents=True)
        with CSV_PATH.open(mode='w', newline='', encoding='utf-8') as _f:
            csv.writer(_f).writerow(csv_columns)  # nosemgrep

    ser_metrics = metrics.dict()
    metrics_row = [ser_metrics[_c] for _c in csv_columns]
    with CSV_PATH.open('a', newline='', encoding='utf-8') as _f:
        csv.writer(_f).writerow(metrics_row)  # nosemgrep
