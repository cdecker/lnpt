from dataclasses import dataclass
from collections.abc import Callable
from typing import Callable, List, Optional


class Context(object):
    pass


Callback = Callable[[Context], None]


@dataclass
class Node:
    """A DAG node representing an atomic step in the protocol."""

    name: str
    func: Callback
    parents: List["Node"]
    children: List["Node"]

    def __str__(self) -> str:
        return f"Node[{self.name}]"

    def __repr__(self) -> str:
        return str(self)
