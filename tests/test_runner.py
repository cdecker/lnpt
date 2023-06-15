import lnpt
from rich.pretty import pprint


def test_simple():
    @lnpt.root(parents=[])
    def start(a):
        print("Start")

    @lnpt.step(parents=[start])
    def step1(a):
        print("Step1")

    @lnpt.step(parents=[start, step1])
    def step2(a):
        print("step2")

    # Check that all nodes are included:
    pprint(lnpt.decorators.nodes)
    assert set([n.func for n in lnpt.decorators.nodes.values()]) == set(
        [start, step1, step2]
    )

    root = lnpt.runner.get_roots(lnpt.decorators.nodes)
    lnpt.runner.graphify(lnpt.decorators.nodes)

    assert len(root) == 1
    assert root[0].func == start
    paths = lnpt.runner.enums(root[0], [])
    print("PATHS", paths)
    funcs = [[p.func for p in path] for path in paths]
    assert funcs == [[start, step1, step2], [start, step2]]
