#!/usr/bin/env python3
import pycpu
import logging

def cpu_fibonacci(cpu):

    # set memory references for eaze of use

    cpu._mem[0] = (cpu._LDI << 8) + 0b00000001
    cpu._mem[1] = (cpu._STA << 8) + 0xe
    cpu._mem[2] = (cpu._LDI << 8) + 0b00000000
    cpu._mem[3] = (cpu._OUT << 8) + 0b00000000
    cpu._mem[4] = (cpu._ADD << 8) + 0xe
    cpu._mem[5] = (cpu._STA << 8) + 0xf
    cpu._mem[6] = (cpu._LDA << 8) + 0xe
    cpu._mem[7] = (cpu._STA << 8) + 0xd
    cpu._mem[8] = (cpu._LDA << 8) + 0xf
    cpu._mem[9] = (cpu._STA << 8) + 0xe
    cpu._mem[10] = (cpu._LDA << 8) + 0xd
    cpu._mem[11] = (cpu._JMP << 8) + 0x3




if __name__ == "__main__":
    testCPU = pycpu.pyCPU()
    testCPU.set_delay(.1)
    cpu_fibonacci(testCPU)
    testCPU.run()

