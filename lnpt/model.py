from dataclasses import dataclass
from collections.abc import Callable
from typing import Callable, List, Optional

@dataclass
class Node():
    """A DAG node representing an atomic step in the protocol.
    """
    name: str
    func: Callable
    parents: List["Node"]
    children: List["Node"]

    def __str__(self):
        return f"Node[{self.name}]"

    def __repr__(self):
        return str(self)
