"""Uninstall files managed by `ttt`."""

import shutil
from pathlib import Path

import platformdirs
from beartype import beartype
from corallium.log import logger

from .. import APP_NAME


@beartype
def get_cache_dir() -> Path:
    """Application cache directory."""
    return Path(platformdirs.user_cache_dir(APP_NAME))


@beartype
def uninstall() -> None:
    """Uninstall files managed by `ttt`."""
    cache_dir = get_cache_dir()
    if cache_dir.is_dir():
        logger.info('Removing cache directory', cache_dir=cache_dir)
        shutil.rmtree(cache_dir)
