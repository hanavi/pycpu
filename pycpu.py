#!/usr/bin/env python3

import sys
import time
import logging

#logging.getLogger().setLevel(logging.DEBUG)

class pyCPU(object):
    def __init__(self):

        # Set up some variables
        self._reg_a = 0
        self._reg_b = 0
        self._pc = 0
        self._jf = 0

        # Current command list
        self._NOP = 0b00000000
        self._LDA = 0b00000001
        self._ADD = 0b00000010
        self._SUB = 0b00000011
        self._LDI = 0b00000100
        self._JMP = 0b00000101
        self._JEZ = 0b00000110
        self._STA = 0b00000111
        self._LDB = 0b00001000
        self._PTA = 0b00001001
        self._ATP = 0b00001010
        # More to be added later?
        self._OUT = 0b00001110
        self._HLT = 0b00001111

        # setup and initialize the memory
        self._mem = []
        for i in range(256):
            self._mem.append(0)

    def nop(self,delay=0):
        if delay > 0:
            time.sleep(delay)
        self._pc += 1

    def lda(self,addr):
        logging.debug(" Loading 0x{:04x} to reg_a".format(addr))
        self._reg_a = self._mem[addr]
        self._pc += 1

    def ldb(self,addr):
        self._reg_b = self._mem[addr]
        self._pc += 1

    def ldi(self,value):
        self._reg_a = value
        self._pc += 1

    def add(self,addr):
        self._reg_b = self._mem[addr]
        self._reg_a = self._reg_a + self._reg_b
        self._pc += 1

    def sub(self,addr):
        self._reg_b = self._mem[addr]
        self._reg_a = self._reg_a - self._reg_b
        self._pc += 1

    def jmp(self,addr):
        self._pc = addr

    def pta(self):
        addr = self._reg_a
        self._reg_a = self._mem[addr]
        self._pc += 1

    def atp(self, addr):
        nAddr = self._mem[addr]
        self._mem[nAddr] = self._reg_a
        self._pc += 1

    def jez(self,addr):
        #print("JEZ: {}".format(self._reg_a))
        if self._reg_a == 0:
            self._pc = addr
        else:
            self._pc += 1

    def out(self):
        print(self._reg_a)
        self._pc += 1

    def hlt(self):
        sys.exit()

    def sta(self,addr):
        self._mem[addr] = self._reg_a
        self._pc += 1

    def run(self):
        while True:
            #time.sleep(1)
            print(self._pc)
            r = self._mem[self._pc]
            logging.debug(' {:016b}'.format(r))
            cmd = r >> 8;
            arg = r & 0b11111111
            logging.debug(" {}: {} {}".format(self._pc,cmd,arg))

            if cmd == self._NOP:
                self.nop()
            elif cmd == self._LDA:
                self.lda(arg)
            elif cmd == self._ADD:
                self.add(arg)
            elif cmd == self._SUB:
                self.sub(arg)
            elif cmd == self._LDI:
                self.ldi(arg)
            elif cmd == self._JMP:
                self.jmp(arg)
            elif cmd == self._JEZ:
                self.jez(arg)
            elif cmd == self._STA:
                self.sta(arg)
            elif cmd == self._LDB:
                self.ldb(arg)
            elif cmd == self._PTA:
                self.pta()
            elif cmd == self._ATP:
                self.atp(arg)
            elif cmd == 11:
                pass
            elif cmd == 12:
                pass
            elif cmd == 13:
                pass
            elif cmd == self._OUT:
                self.out()
            elif cmd == self._HLT:
                self.hlt();
            else:
                print("Shouldn't be here...")
                sys.exit()

    def dumpMemory(self):
        for i in range(255):
            print('{:02x}: {:016b}'.format(i,self._mem[i]))


if __name__ == "__main__":
    testCPU = pyCPU()
    testCPU.dumpMemory()
    #testCPU.run()




