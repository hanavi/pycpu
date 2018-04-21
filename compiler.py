#!/usr/bin/env python3

import numpy as np

def load_file(fname):
    fd = open(fname)
    data = fd.readlines()
    return data

def convert(filedata):

    mc = [] # machine code for the ram
    for line in filedata:
        mc.append(get_binary(line.strip()))
    return mc

def get_binary(line):
    cmd = line.split(" ")
    ret = None

    # Current command list
    NOP = 0b00000000
    LDA = 0b00000001
    ADD = 0b00000010
    SUB = 0b00000011
    LDI = 0b00000100
    JMP = 0b00000101
    JEZ = 0b00000110
    STA = 0b00000111
    LDB = 0b00001000
    PTA = 0b00001001
    ATP = 0b00001010
    OUT = 0b00001110
    HLT = 0b00001111

    if cmd[0] == "nop":
        ret = 0b0
    elif cmd[0] == "lda":
        ret = (LDA << 8) + int((cmd[1]),16)
    elif cmd[0] == "add":
        ret = (ADD << 8) + int((cmd[1]),16)
    elif cmd[0] == "sub":
        ret = (SUB << 8) + int((cmd[1]),16)
    elif cmd[0] == "ldi":
        ret = (LDI << 8) + int((cmd[1]),16)
    elif cmd[0] == "jmp":
        ret = (JMP << 8) + int((cmd[1]),16)
    elif cmd[0] == "jez":
        ret = (JEZ << 8) + int((cmd[1]),16)
    elif cmd[0] == "sta":
        ret = (STA << 8) + int((cmd[1]),16)
    elif cmd[0] == "ldb":
        ret = (LDB << 8) + int((cmd[1]),16)
    elif cmd[0] == "pta":
        ret = (PTA << 8) + 0b00000000
    elif cmd[0] == "atp":
        ret = (ATP << 8) + int((cmd[1]),16)
    elif cmd[0] == "out":
        ret = (OUT << 8) + 0b00000000
    elif cmd[0] == "hlt":
        ret = (HLT << 8) + 0b00000000

    return ret

def save_prog(bdata,ofname):
    np.savetxt(ofname,bdata,fmt='%d')

if __name__ == "__main__":
    fname = "program_2.in"
    ofname = "program_2.pc"
    data = load_file(fname)
    bdata = convert(data)
    save_prog(bdata,ofname)
