import random
import time

file = open("code", "r")
code = file.read()

userfile = ""
usercode = ""
userptr = 0
useropen = False


i = 0
word = ""

cell = [0]
cellptr = 0
numofcells = 1
stack = []

while 1:
    if code[i] not in ["\n", ";", "#"]:
        word += code[i]
    if code[i] == "#":
        i += 1
        while code[i] != "#":
            i += 1

    #print(word)
    #print(stack)

    if word == "set cell as ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "stack":
            cell[cellptr] = stack.pop()
        elif word == "input":
            x = input(">: ")
            try:
                cell[cellptr] = int(x)
            except:
                cell[cellptr] = ord(x)
        elif word == "file":
            x = usercode[userptr]
            try:
                cell[cellptr] = int(x)
            except:
                cell[cellptr] = ord(x)
            userptr += 1
        else:
            cell[cellptr] = int(word)
        word = ""
    
    elif word == "push onto stack ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "cell":
            stack.append(cell[cellptr])
        else:
            stack.append(int(word))
        word = ""

    elif word == "move pointer to the right.":
        cellptr += 1
        if cellptr == numofcells:
            cell.append(0)
            numofcells += 1 
        word = ""
    
    elif word == "move pointer to the left.":
        cellptr -= 1
        word = ""

    elif word == "move pointer to cell ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "cell":
            cellptr = cell[cellptr]
        else:
            cellptr = int(word)
        while cellptr >= numofcells:
            cell.append(0)
            numofcells += 1 
        word = ""

    elif word == "output cell as ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "number":
            print(cell[cellptr], end="")
        elif word == "character":
            print(chr(cell[cellptr]), end="") 
        word = ""        

    elif word == "output string ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        print(word)
        word = ""         

    elif word == "increase cell by ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "stack":
            cell[cellptr] += stack.pop()
        else:
            cell[cellptr] += int(word)
        word = ""  

    elif word == "decrease cell by":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "stack":
            cell[cellptr] -= stack.pop()
        else:
            cell[cellptr] -= int(word)
        word = "" 

    elif word == "multiply cell by ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "stack":
            cell[cellptr] *= stack.pop()
        else:
            cell[cellptr] *= int(word)
        word = "" 

    elif word == "divide cell by ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "stack":
            cell[cellptr] //= stack.pop()
        else:
            cell[cellptr] //= int(word)
        word = "" 

    elif word == "modulus cell by ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "stack":
            cell[cellptr] %= stack.pop()
        else:
            cell[cellptr] %= int(word)
        word = "" 

    elif word == "raise cell to the power of ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "stack":
            cell[cellptr] **= stack.pop()
        else:
            cell[cellptr] **= int(word)
        word = "" 

    elif word == "if cell equals ":
        word = ""
        i += 1
        while code[i] != ":":
            word += code[i]
            i += 1
        if word == "stack":
            x = stack.pop()
        else:
            x = int(word)
        if cell[cellptr] != x:
            x = 1
            while x != 0:
                i += 1
                if code[i] == ":":
                    x += 1
                elif code[i] == ";":
                    x -= 1
        word = "" 

    elif word == "if cell is less than ":
        word = ""
        i += 1
        while code[i] != ":":
            word += code[i]
            i += 1
        if word == "stack":
            x = stack.pop()
        else:
            x = int(word)
        if not cell[cellptr] < x:
            x = 1
            while x != 0:
                i += 1
                if code[i] == ":":
                    x += 1
                elif code[i] == ";":
                    x -= 1
        word = "" 

    elif word == "if cell is larger than ":
        word = ""
        i += 1
        while code[i] != ":":
            word += code[i]
            i += 1
        if word == "stack":
            x = stack.pop()
        else:
            x = int(word)
        if not cell[cellptr] > x:
            x = 1
            while x != 0:
                i += 1
                if code[i] == ":":
                    x += 1
                elif code[i] == ";":
                    x -= 1
        word = "" 

    elif word == "jump to line ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "cell":
            x = cell[cellptr]
        else:
            x = int(word) - 1
        i = 0
        for y in range(x):
            while code[i] != "\n":
                i += 1
            i += 1
        i -= 1
        word = ""

    elif word == "randomize cell as a number between 0 and ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "cell":
            cell[cellptr] = random.randrange(cell[cellptr]+1)
        else:
            cell[cellptr] = random.randrange(int(word)+1)
        word = "" 

    elif word == "read file ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        userfile = open(word, "r+")
        usercode = userfile.read()
        word = ""  

    elif word == "write to file ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        userfile.write(word)
        word = ""  

    elif word == "move file pointer left":
        userptr -= 1        
        word = "" 
    
    elif word == "halt program for ":
        word = ""
        i += 1
        while code[i] != ".":
            word += code[i]
            i += 1
        if word == "cell":
            time.sleep(cell[cellptr])
        else:
            time.sleep(int(word))
        word = ""      

    elif word == " ":
        word = "" 

    elif word == "end program.":
        break

    i += 1
    
if userfile == True:
    userfile.close()
file.close()
