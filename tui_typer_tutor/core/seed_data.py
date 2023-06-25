"""Load Seed Data."""

import random
from pathlib import Path

from beartype import beartype

from .typing import ExpectedKey

DEFAULT_SEED_FILE = Path(__file__).with_suffix('.txt')


@beartype
def load_seed_data(seed_text: str) -> list[ExpectedKey]:
    """Load Seed Data in Vim format."""
    grouped_keys = []
    for line in seed_text.split('\n'):
        keys = []
        token = ''
        for char in line:
            token += char
            if not token.startswith('<') or token.endswith('>'):
                keys.append(ExpectedKey(raw=token))
                token = ''
        if token:
            keys.append(ExpectedKey(raw=token))
        grouped_keys.append(keys)
    random.shuffle(grouped_keys)  # noqa: DUO102
    return [_k for _keys in grouped_keys for _k in _keys]
