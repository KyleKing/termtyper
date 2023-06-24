"""Extend Invoke for gh-ops."""

from types import ModuleType

from beartype import beartype
from beartype.typing import Optional
from invoke.collection import Collection
from invoke.program import Program


# PLANNED: Reduce the non-gh-ops output from Invoke
#  https://docs.pyinvoke.org/en/stable/concepts/library.html
@beartype
def start_program(  # pragma: no cover
    pkg_name: str,
    pkg_version: str,
    module: Optional[ModuleType] | None = None,
    collection: Optional[Collection] | None = None,
) -> None:
    """Run the customized Invoke Program."""
    Program(
        name=pkg_name,
        version=pkg_version,
        namespace=Collection.from_module(module) if module else collection,
    ).run()
