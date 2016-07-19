import numpy as np
from platform import python_version
import pynbody


def run():
    print("hello world")

    a = 7

    print(a)

    print(np.random.rand(3, 1))

    print(python_version())

    f = pynbody.load("/Users/nroth/Projects/spin/simulations/ref105snaps/snapshot_104")
    print(f[0]['pos'])
