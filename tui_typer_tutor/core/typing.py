"""Typing Logic."""

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


class TypedKey(ExpectedKey):
    """Typed Key."""

    expected: ExpectedKey
    """Store the expected key when typed and expected become out-of-sync."""

    @property
    def was_correct(self) -> bool:
        """If typed key matches expected."""
        return self.text == self.expected.text


class Keys(BaseModel):
    """Key Model."""

    expected: list[ExpectedKey] = Field(default_factory=list)
    """The expected keys for practice."""

    typed_all: list[TypedKey] = Field(default_factory=list)
    """Append-only."""

    typed: list[TypedKey] = Field(default_factory=list)
    """ONly tracks non-deleted keys."""

    last_was_delete: bool = False
    """Indicate if last operation was a delete."""

    @beartype
    def store(self, key: TypedKey) -> None:
        """Store a new typed key."""
        self.typed_all.append(key)
        self.last_was_delete = key.raw == 'backspace'
        if self.last_was_delete:
            if self.typed:
                self.typed = self.typed[:-1]
        else:
            self.typed.append(key)


@beartype
def on_keypress(raw: str, keys: Keys) -> Keys:
    """Process a key press."""
    expected = keys.expected[len(keys.typed)]
    key = TypedKey(raw=raw, expected=expected)
    keys.store(key)
    return keys
