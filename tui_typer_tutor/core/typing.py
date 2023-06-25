"""Typing Logic."""

import bisect

from beartype import beartype
from pydantic import BaseModel, Field

from ..constants import VIM_TO_TEXTUAL


class ExpectedKey(BaseModel):
    """Expected Key."""

    raw: str
    """Textual Key Name."""

    @property
    def text(self) -> str:
        """Displayed text."""
        return VIM_TO_TEXTUAL.inverse.get(self.raw) or self.raw

    @property
    def width(self) -> int:
        """Displayed text."""
        return len(self.text)


class TypedKey(ExpectedKey):
    """Typed Key."""

    expected: ExpectedKey
    """Store the expected key when typed and expected become out-of-sync."""

    @property
    def was_correct(self) -> bool:
        """If typed key matches expected."""
        return self.text == self.expected.text


class _KeysAccum(BaseModel):
    """Histogram-style store for identifying character widths."""

    expected: list[int] = Field(default_factory=list)
    """Accumulating count of character width per Key."""

    typed: list[int] = Field(default_factory=list)
    """Accumulating count of character width per Key."""

    @beartype
    def get_indices(self, accum: list[int], start: int, end: int) -> tuple[int, int]:
        """Return the adjusted start and end."""
        adj_start = bisect.bisect(accum, start)
        adj_end = bisect.bisect(accum, end - start + adj_start) if len(accum) > end else len(accum)
        return (adj_start, adj_end)


class Keys(BaseModel):
    """Key Model."""

    expected: list[ExpectedKey] = Field(default_factory=list)
    """The expected keys for practice."""

    typed_all: list[TypedKey] = Field(default_factory=list)
    """Append-only."""

    typed: list[TypedKey] = Field(default_factory=list)
    """Only tracks non-deleted keys."""

    last_was_delete: bool = False
    """Indicate if last operation was a delete."""

    accum: _KeysAccum = Field(default_factory=_KeysAccum)
    """Accumulating index store (private)."""

    def copy(self) -> 'Keys':
        """Ensure that the lists are deep-copied."""
        keys = super().copy()
        keys.expected = [*keys.expected]
        keys.typed_all = [*keys.typed_all]
        keys.typed = [*keys.typed]
        keys.accum.expected = [*keys.accum.expected]
        keys.accum.typed = [*keys.accum.typed]
        return keys

    @beartype
    def get_expected(self, start: int, end: int) -> list[ExpectedKey]:
        """Retrieve the next page of expected keys."""
        if not self.accum.expected:  # Lazily evaluate the expected values
            counter = 0
            for exp in self.expected:
                counter += exp.width
                self.accum.expected.append(counter)
        adj_start, adj_end = self.accum.get_indices(self.accum.expected, start, end)
        return self.expected[adj_start:adj_end]

    @beartype
    def get_typed(self, start: int, end: int) -> list[TypedKey]:
        """Retrieve the next page of typed keys."""
        adj_start, adj_end = self.accum.get_indices(self.accum.typed, start, end)
        return self.typed[adj_start:adj_end]

    @beartype
    def store(self, key: TypedKey) -> None:
        """Store a new typed key."""
        self.typed_all.append(key)
        self.last_was_delete = key.raw == 'backspace'
        if self.last_was_delete:
            if self.typed:
                self.typed = self.typed[:-1]
                self.accum.typed.pop()
        else:
            self.typed.append(key)
            counter = (self.accum.typed or [0])[-1]
            self.accum.typed.append(counter + key.width)


@beartype
def on_keypress(raw: str, keys: Keys) -> None:
    """Process a key press."""
    expected = keys.expected[len(keys.typed)]
    key = TypedKey(raw=raw, expected=expected)
    keys.store(key)
