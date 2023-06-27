"""Global variables for testing."""

from pathlib import Path

import arrow
from beartype import beartype
from corallium.file_helpers import delete_dir, ensure_dir

TEST_DIR = Path(__file__).resolve().parent
"""Path to the `test` directory that contains this file and all other tests."""

TEST_DATA_DIR = TEST_DIR / 'data'
"""Path to subdirectory with test data within the Test Directory."""

TEST_TMP_CACHE = TEST_DIR / '_tmp_cache'
"""Path to the temporary cache folder in the Test directory."""


def clear_test_cache() -> None:
    """Remove the test cache directory if present."""
    delete_dir(TEST_TMP_CACHE)
    ensure_dir(TEST_TMP_CACHE)


FROZEN_TIME = arrow.get('2025-01-02T14:05:06+00:00').datetime
"""Frozen timestamp used for testing when needed."""


@beartype
def stubbed_user_cache_dir(appname: str | None = None) -> str:
    """Stub `platformdirs.user_cache_dir`."""
    return (TEST_TMP_CACHE / (appname or 'user_cache_dir')).as_posix()
