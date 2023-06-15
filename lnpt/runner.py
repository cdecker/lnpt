from lnpt.decorators import nodes
from rich.pretty import pprint
from typing import List, Dict
from lnpt.model import Node, Callback, Context


def graphify(nodes: Dict[Callback, Node]) -> None:
    # We start by collecting all the children for each node.
    for _, n in nodes.items():
        for p in n.parents:
            p.children.append(n)


def get_roots(nodes: Dict[Callback, Node]) -> List[Node]:
    roots = []
    for _, n in nodes.items():
        if n.parents == []:
            roots.append(n)

    return roots


def enums(s: Node, prefix: List[Node]) -> List[List[Node]]:
    prefix += [s]

    # No children? We must be a terminal state, so the prefix fully
    # describes how we got here.
    if s.children == []:
        return [prefix]

    # Not a terminal state? Well then we need to recurse further
    collected = []
    for c in s.children:
        collected.extend(enums(c, prefix.copy()))

    return collected


def execute(path: List[Node]) -> None:
    """Run a single path through the protocol DAG."""
    ctx = Context()
    for n in path:
        print(f"Executing step {n}")
        n.func(ctx)
        print(f"Step {n} returned")


def run() -> None:
    graphify(nodes)
    roots = get_roots(nodes)
    paths: List[List[Node]] = enums(roots[0], [])
    pprint(paths)
    for p in paths:
        print(f"Executing path {p}")
        execute(p)
