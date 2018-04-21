#!/usr/bin/env python3

import numpy as np
import pycpu

def load_prog(fname):
    data = np.loadtxt(fname,dtype="int")
    return data

if __name__ == "__main__":
    data = load_prog("program_2.pc")
    testCPU = pycpu.pyCPU()
    testCPU.load(data)
    testCPU.set_delay(.1)
    testCPU.run()
