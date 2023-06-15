from lnpt.model import Node, Context, Callback
from typing import Dict, Callable, List, Any

nodes: Dict[Callback, Node] = {}  # func -> Node


DecoratedCallback = Callable[[Callback], Callback]


def root(parents: List[Callback]) -> DecoratedCallback:
    def inner(func: Callback) -> Callback:
        global nodes

        pars = [nodes[p] for p in parents]

        nodes[func] = Node(name=func.__name__, func=func, parents=pars, children=[])
        return func

    return inner


def step(parents: List[Callback]) -> DecoratedCallback:
    def inner(func: Callback) -> Callback:
        global nodes
        pars = [nodes[p] for p in parents]
        nodes[func] = Node(name=func.__name__, func=func, parents=pars, children=[])
        return func

    return inner


def leaf(parents: List[Callback]) -> DecoratedCallback:
    def inner(func: Callback) -> Callback:
        global nodes
        pars = [nodes[p] for p in parents]
        nodes[func] = Node(name=func.__name__, func=func, parents=pars, children=[])
        return func

    return inner
