#!/usr/bin/env python3

import logging
import pycpu

def cpu_multiply(a,b,cpu):

    # set memory references for eaze of use
    tAddr = 18
    m = tAddr + 20
    r = 2

    cpu._mem[0] = (cpu._LDI << 8) + 0b00000101
    cpu._mem[1] = (cpu._JMP << 8) + tAddr
    cpu._mem[2] = (cpu._LDA << 8) + 0b00000101
    cpu._mem[3] = (cpu._OUT << 8) + 0b00000000
    cpu._mem[4] = (cpu._HLT << 8) + 0b00000000
    cpu._mem[5] = a
    cpu._mem[6] = b

    ####################################################################
    # Test function: multiplication
    ####################################################################


    # Get the address of the first variable from reg_a and
    # save it where we can get to it
    cpu._mem[tAddr] = (cpu._STA << 8) + m

    logging.debug(" -- {:016b}".format(cpu._PTA))
    logging.debug(" -- {:016b}".format(cpu._PTA<<8))

    # Get the value of the first variable and save it locally
    cpu._mem[tAddr + 1] = (cpu._PTA << 8) + 0b00000000
    cpu._mem[tAddr + 2] = (cpu._STA << 8) + m + 1

    # Get the value of the second variable and save it locally
    cpu._mem[tAddr + 3] = (cpu._LDI << 8) + 1
    cpu._mem[tAddr + 4] = (cpu._ADD << 8) + m
    cpu._mem[tAddr + 5] = (cpu._PTA << 8) + 0b00000000
    cpu._mem[tAddr + 6] = (cpu._STA << 8) + m + 2

    # Set up our "addition loop" for multiplying
    cpu._mem[tAddr + 7] = (cpu._LDI << 8) + 0
    cpu._mem[tAddr + 8] = (cpu._STA << 8) + m + 3
    cpu._mem[tAddr + 9] = (cpu._LDI << 8) + 1
    cpu._mem[tAddr + 10] = (cpu._STA << 8) + m + 4

    # Do our loop work
    cpu._mem[tAddr + 11] = (cpu._LDA << 8) + m + 3
    cpu._mem[tAddr + 12] = (cpu._ADD << 8) + m + 1
    cpu._mem[tAddr + 13] = (cpu._STA << 8) + m + 3

    # Save the value to the original address
    cpu._mem[tAddr + 14] = (cpu._ATP << 8) + m

    # Decrement the multiplier
    cpu._mem[tAddr + 15] = (cpu._LDA << 8) + m + 2
    cpu._mem[tAddr + 16] = (cpu._SUB << 8) + m + 4
    cpu._mem[tAddr + 17] = (cpu._STA << 8) + m + 2

    # Check to see if we are done
    cpu._mem[tAddr + 18] = (cpu._JEZ << 8) + r
    cpu._mem[tAddr + 19] = (cpu._JMP << 8) + tAddr + 11

if __name__ == "__main__":
    testCPU = pycpu.pyCPU()
    cpu_multiply(33,58,testCPU)
    print("actual: {}".format(33*58))
    testCPU.run()
