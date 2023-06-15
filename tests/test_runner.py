import lnpt
from rich.pretty import pprint


@lnpt.root(parents=[])
def start(a):
    print("Start")

@lnpt.step(parents=[start])
def step1(a):
    print("Step1")

@lnpt.step(parents=[start, step1])
def step2(a):
    print('step2')

lnpt.run()
