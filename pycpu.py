#!/usr/bin/env python3

import sys
import time
import logging

#logging.getLogger().setLevel(logging.DEBUG)

class pyCPU(object):
    def __init__(self):

        # Set up some variables
        self._reg_a = 0 # Register A
        self._reg_b = 0 # Register B
        self._pc = 0    # Program Counter
        self._jf = 0    # Jump flag (not implemented yet)
        self._delay = 0 # We can use this to slow down our cpu a bit

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
        # Gap here for more cmds
        self._OUT = 0b00001110
        self._HLT = 0b00001111

        # setup and initialize the memory
        self._mem = []
        for i in range(256):
            self._mem.append(0)

    def _nop(self,delay=0):
        """ NOP: Do nothing """

        if delay > 0:
            time.sleep(delay)
        self._pc += 1

    def _lda(self,addr):
        """ Load the value of addr to reg_a """

        logging.debug(" Loading 0x{:04x} to reg_a".format(addr))
        self._reg_a = self._mem[addr]
        self._pc += 1

    def _ldb(self,addr):
        """ Load the value of addr to reg_b """

        self._reg_b = self._mem[addr]
        self._pc += 1

    def _ldi(self,value):
        """ Load the given value to reg_a """

        self._reg_a = value
        self._pc += 1

    def _add(self,addr):
        """ Add the value in addr to the reg_a and place in reg_a """

        self._reg_b = self._mem[addr]
        self._reg_a = self._reg_a + self._reg_b
        self._pc += 1

    def _sub(self,addr):
        """ Subtract the value in addr from the value in reg_a and place in reg_a """

        self._reg_b = self._mem[addr]
        self._reg_a = self._reg_a - self._reg_b
        self._pc += 1

    def _jmp(self,addr):
        """ Jump to addr """

        self._pc = addr

    def _pta(self):
        """ Place the value from the address in addr into reg_a (pointer) """

        addr = self._reg_a
        self._reg_a = self._mem[addr]
        self._pc += 1

    def _atp(self, addr):
        """ Place the value into the address in addr from reg_a (pointer) """

        nAddr = self._mem[addr]
        self._mem[nAddr] = self._reg_a
        self._pc += 1

    def _jez(self,addr):
        """ Jump if the value in reg_a is 0 """

        #print("JEZ: {}".format(self._reg_a))
        if self._reg_a == 0:
            self._pc = addr
        else:
            self._pc += 1

    def _out(self):
        """ Print out the results in reg_a """

        print(self._reg_a)
        self._pc += 1

    def _hlt(self):
        """ Halt the program """

        sys.exit()

    def _sta(self,addr):
        """ Store the value in reg_a to addr """

        self._mem[addr] = self._reg_a
        self._pc += 1

    def set_delay(self,delay):
        self._delay = delay

    def run(self):
        """ Run the program """

        while True:
            time.sleep(self._delay) # Slow down our cpu a bit
            r = self._mem[self._pc] # Get the command from memory
            cmd = r >> 8;
            arg = r & 0b11111111

            logging.debug(' {:016b}'.format(r))
            logging.debug(" {}: {} {}".format(self._pc,cmd,arg))

            if cmd == self._NOP:
                self._nop()
            elif cmd == self._LDA:
                self._lda(arg)
            elif cmd == self._ADD:
                self._add(arg)
            elif cmd == self._SUB:
                self._sub(arg)
            elif cmd == self._LDI:
                self._ldi(arg)
            elif cmd == self._JMP:
                self._jmp(arg)
            elif cmd == self._JEZ:
                self._jez(arg)
            elif cmd == self._STA:
                self._sta(arg)
            elif cmd == self._LDB:
                self._ldb(arg)
            elif cmd == self._PTA:
                self._pta()
            elif cmd == self._ATP:
                self._atp(arg)
            elif cmd == 11:
                pass
            elif cmd == 12:
                pass
            elif cmd == 13:
                pass
            elif cmd == self._OUT:
                self._out()
            elif cmd == self._HLT:
                self._hlt();
            else:
                print("Shouldn't be here...")
                sys.exit()

    def dumpMemory(self):
        for i in range(255):
            print('{:02x}: {:016b}'.format(i,self._mem[i]))


if __name__ == "__main__":
    testCPU = pyCPU()
    testCPU.dumpMemory()
    testCPU.run()




