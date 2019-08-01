#Advanced Computer Language --> Python port

import random

class ACL:
    def getCode(self) -> str:
        try:
            print("File to interpret? ")
            fileName: str = input()

            file = open(fileName)
            code: str = file.read()
            file.close()

            return code
        except FileNotFoundError as e:
            print("FILE FAIL")
            return "F"

    def toDec(self, _bin: str) -> int:
        l: int = len(_bin)
        j: int = l - 1
        x: int = 0
        dec: int = 0
        while x < l:
            dec += (2 ** x) * (ord(_bin[j]) - 48)
            x += 1; j -= 1

        return dec

    def main(self):

        #declares necessary variables etc.
        
        code: str = self.getCode()
        l: int = len(code)
        i: int = 0 #code reader pointer

        memory: list(int) = list() #cell based, binary
        memory.append(int(0)) #make the memory have one cell at start
        ptr: int = 0 #memory pointer
        cells: int = 1 #cells in memory

        bOutput: str = "" #binary output
        cOutput: str = "" #character output
        c: str = "" #code command

        f: str = "" #for functions

        #temporary variables
        t: str = ""
        x: int = 0


        #--------------------

        #inserts function code when function call
        #pre-execution
        while i < l:
            c = code[i]
            #declare function
            if c == "D":
                i += 1
                f = ""
                while code[i] != "D":
                    f += code[i]
                    i += 1
            #enter function into code
            elif c == "E":
                t = ""
                for x in range(0, i + 1):
                    t += code[x]
                t += f

                for x in range(i + 1, l):
                    t += code[x]

                code = t
                l = len(code)

            i += 1

        i = 0

        #--------------------

        while i < l:
            c = code[i]

            #pointer movement
            if c == "0":
                ptr = 0

            elif c == "1":
                ptr += 1
                if ptr == cells:
                    memory.append(int(0))
                    cells += 1


            elif c == "2":
                ptr -= 1
                if ptr < 0:
                    ptr = cells - 1

            #bit flip
            elif c == "3":
                if memory[ptr] == 1:
                    memory[ptr] = int(0)
                else:
                    memory[ptr] = int(1)

            elif c == "4":
                bOutput += str(memory[ptr])

            #if-else-endif
            elif c == "5":
                if memory[ptr] == 0:
                    x = 1
                    while x != 0:
                        i += 1
                        if code[i] == '5':
                            x += 1
                        elif code[i] == "7" or (x == 1 and code[i] == "6"):
                            x -= 1

            #else
            elif c == "6":
                x = 1
                while x != 0:
                    i += 1
                    if code[i] == "5":
                        x += 1
                    elif code[i] == "7":
                        x -= 1

            elif c == "7":
                #endif command, does nothing on its own
                pass

            #loop
            elif c == "8":
                if memory[ptr] == 1:
                    x = 1
                    i -= 1
                    while x != 0:
                        i -= 1
                        
                        if code[i] == "7":
                            x += 1
                        elif code[i] == "5":
                            x -= 1

            elif c == "9":
                memory[ptr] = int(round(random.random()))

            #input
            elif c == "A":
                x = int(input())
                if (x != 0 and x != 1):
                    print(1111)
                    i = l

                else:
                    memory[ptr] = int(x)

            #binary output
            elif c == "B":
                print(bOutput)
                bOutput = ""

            #integer and character output
            elif c == "C":
                if bOutput == "":
                    print(cOutput)
                    cOutput = ""
                elif memory[ptr] == 1:
                    cOutput += str(self.toDec(bOutput))
                else:
                    cOutput += str(chr(self.toDec(bOutput)))

                bOutput = ""

            elif c == "D":
                pass

            elif c == "E":
                #D and E are handled pre-execution
                pass

            elif c == "F":
                print(1111)
                i = l

            i += 1


interpreter = ACL()
interpreter.main()

