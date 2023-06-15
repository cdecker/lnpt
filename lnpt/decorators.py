from lnpt.model import Node
from typing import Dict, Callable, List


nodes: Dict[Callable, Node] = {}  # func -> Node

def root(parents=List[Callable], *args, **kwargs):
    print("Ctor", args, kwargs)
    def inner(func):
        global nodes

        pars = [nodes[p] for p in parents]
        print(pars)
        
        nodes[func] = Node(
            name=func.__name__,
            func=func,
            parents=pars,
            children=[]
        )
        return func
    return inner


def step(parents: List[Callable], *args, **kwargs):
    def inner(func):
        global nodes
        pars = [nodes[p] for p in parents]
        print(pars)
        nodes[func] = Node(
            name=func.__name__,
            func=func, parents=pars, children=[])
        return func
    return inner

def leaf(parents: List[Callable], *args, **kwargs):
    def inner(func):
        global nodes
        pars = [nodes[p] for p in parents]
        nodes[func] = Node(
            name=func.__name__,
            func=func, parents=pars, children=[])
        return func
    return inner
