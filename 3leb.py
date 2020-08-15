#3LEB

import random
import os 
import time

code = open("code", "r")
code = code.read()

stack = []

var = []
val = []

fname = []
fcont = []

i = 0
while 1:

    word = ""    
    while code[i] not in [" ", "\n"]:
        word += code[i]
        i += 1

    if word == "PEB":
        while code[i] != "[":
            i += 1
        word = ""
        i += 1
        while code[i] != "]":
            word += code[i]
            i += 1
        i += 1
        while code[i] == " ":
            i += 1
        arg = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                arg += code[i]
                i += 1
            ind = var.index(arg)
            arg = int(val[ind])
        else:
            while code[i] != "\n":
                arg += code[i]
                i += 1
        if word not in var:
            var.append(word)
            val.append(0)
        ind = var.index(word)
        val[ind] = int(arg)

    if word == "GUN":
        while code[i] != "[":
            i += 1
        word = ""
        i += 1
        while code[i] != "]":
            word += code[i]
            i += 1
        i += 1
        while code[i] == " ":
            i += 1
        arg = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                arg += code[i]
                i += 1
            ind = var.index(arg)
            arg = int(val[ind])
        else:
            while code[i] != "\n":
                arg += code[i]
                i += 1
        ind = var.index(word)
        val[ind] += int(arg)

    if word == "HYL":
        while code[i] != "[":
            i += 1
        word = ""
        i += 1
        while code[i] != "]":
            word += code[i]
            i += 1
        i += 1
        while code[i] == " ":
            i += 1
        arg = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                arg += code[i]
                i += 1
            ind = var.index(arg)
            arg = int(val[ind])
        else:
            while code[i] != "\n":
                arg += code[i]
                i += 1
        ind = var.index(word)
        val[ind] -= int(arg)

    if word == "AMY":
        while code[i] != "[":
            i += 1
        word = ""
        i += 1
        while code[i] != "]":
            word += code[i]
            i += 1
        i += 1
        while code[i] == " ":
            i += 1
        arg = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                arg += code[i]
                i += 1
            ind = var.index(arg)
            arg = int(val[ind])
        else:
            while code[i] != "\n":
                arg += code[i]
                i += 1
        ind = var.index(word)
        val[ind] *= int(arg)

    if word == "PLE":
        while code[i] != "[":
            i += 1
        word = ""
        i += 1
        while code[i] != "]":
            word += code[i]
            i += 1
        i += 1
        while code[i] == " ":
            i += 1
        arg = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                arg += code[i]
                i += 1
            ind = var.index(arg)
            arg = int(val[ind])
        else:
            while code[i] != "\n":
                arg += code[i]
                i += 1
        ind = var.index(word)
        val[ind] //= int(arg)

    if word == "ROV":
        while code[i] != "[":
            i += 1
        word = ""
        i += 1
        while code[i] != "]":
            word += code[i]
            i += 1
        i += 1
        while code[i] == " ":
            i += 1
        arg = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                arg += code[i]
                i += 1
            ind = var.index(arg)
            arg = int(val[ind])
        else:
            while code[i] != "\n":
                arg += code[i]
                i += 1
        ind = var.index(word)
        val[ind] %= int(arg)

    elif word == "JAO":
        i += 1
        while code[i] == " ":
            i += 1
        word = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                word += code[i]            
                i += 1
            ind = var.index(word)
            word = val[ind]
        else:
            while code[i] != "\n":
                word += code[i]
                i += 1            
        print(word, end="")

    elif word == "GAU":       
        i += 1
        while code[i] == " ":
            i += 1
        word = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                word += code[i]            
                i += 1
            ind = var.index(word)
            word = val[ind]
        else:
            while code[i] != "\n":
                word += code[i]
                i += 1
            word = int(word)
        print(chr(word), end="")
        
    elif word == "UNA":
        while code[i] != "[":
            i += 1
        i += 1
        word = ""
        while code[i] != "]":
            word += code[i]
            i += 1
        ind = var.index(word)
        val[ind] = int(input(">"))

    elif word == ".IK":
        while code[i] != "[":
            i += 1
        i += 1
        word = ""
        while code[i] != "]":
            word += code[i]
            i += 1
        i += 1
        while code[i] == " ":
            i += 1
        oper = ""        
        while code[i] != " ":
            oper += code[i]
            i += 1
        while code[i] == " ":
            i += 1
        arg = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                arg += code[i]
                i += 1
            ind = var.index(arg)
            arg = int(val[ind])
        else:
            while code[i] != "\n":
                arg += code[i]
                i += 1
            arg = int(arg)
        ind = var.index(word)   
        word = val[ind]
        if oper == "AOS" and word != arg:
            x = 1
            while x != 0:
                i += 1
                if code[i] == ".":
                    x += 1
                elif code[i] == ",":
                    x -= 1
        elif oper == "SEB" and word == arg:
            x = 1
            while x != 0:
                i += 1
                if code[i] == ".":
                    x += 1
                elif code[i] == ",":
                    x -= 1
        elif oper == "IDI" and word <= arg:
            x = 1
            while x != 0:
                i += 1
                if code[i] == ".":
                    x += 1
                elif code[i] == ",":
                    x -= 1
        elif oper == "VEA" and word >= arg:
            x = 1
            while x != 0:
                i += 1
                if code[i] == ".":
                    x += 1
                elif code[i] == ",":
                    x -= 1

    elif word == ":LY":
        while code[i] != "[":
            i += 1
        i += 1
        word = ""
        while code[i] != "]":
            word += code[i]
            i += 1
        i += 1
        while code[i] == " ":
            i += 1
        oper = ""        
        while code[i] != " ":
            oper += code[i]
            i += 1
        while code[i] == " ":
            i += 1
        arg = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                arg += code[i]
                i += 1
            ind = var.index(arg)
            arg = int(val[ind])
        else:
            while code[i] != "\n":
                arg += code[i]
                i += 1
            arg = int(arg)
        ind = var.index(word)   
        word = val[ind]
        if oper == "AOS" and word != arg:
            x = 1
            while x != 0:
                i += 1
                if code[i] == ":":
                    x += 1
                elif code[i] == ";":
                    x -= 1
        elif oper == "SEB" and word == arg:
            x = 1
            while x != 0:
                i += 1
                if code[i] == ":":
                    x += 1
                elif code[i] == ";":
                    x -= 1
        elif oper == "IDI" and word <= arg:
            x = 1
            while x != 0:
                i += 1
                if code[i] == ":":
                    x += 1
                elif code[i] == ";":
                    x -= 1
        elif oper == "VEA" and word >= arg:
            x = 1
            while x != 0:
                i += 1
                if code[i] == ":":
                    x += 1
                elif code[i] == ";":
                    x -= 1

    elif word == ";":
        x = 1
        i -= 1
        while x != 0:
            i -= 1
            if code[i] == ";":
                x += 1
            elif code[i] == ":":
                x -= 1
        i -= 1  

    elif word == "ILO":
        x = 1
        while x != 0:
            i -= 1
            if code[i] == ";":
                x += 1
            elif code[i] == ":":
                x -= 1
        i -= 1 

    elif word == "GAN":
        x = 1
        while x != 0:
            i += 1
            if code[i] == ":":
                x += 1
            elif code[i] == ";":
                x -= 1

    elif word == "VAN":
        while code[i] != "[":
            i += 1
        i += 1
        word = ""
        while code[i] != "]":
            word += code[i]            
            i += 1
        i += 1
        while code[i] == " ":
            i += 1
        arg = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                arg += code[i]            
                i += 1
            ind = var.index(arg)
            arg = val[ind]
        else:
            while code[i] != "\n":
                arg += code[i]
                i += 1
            arg = int(arg)
        ind = var.index(word)
        val[ind] = random.randrange(arg+1)        

    elif word == "RAY":
        i += 1
        while code[i] == " ":
            i += 1
        word = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                word += code[i]                 
                i += 1
            ind = var.index(word)
            word = val[ind]
        else:
            while code[i] != "\n":
                word += code[i]
                i += 1
            word = int(word)
        stack.append(word) 

    elif word == "MIG":           
        while code[i] != "[":
            i += 1
        i += 1
        word = ""
        while code[i] != "]":
            word += code[i]
            i += 1
        ind = var.index(word)
        val[ind] = stack.pop()

    elif word == "HAF":
        while code[i] != "[":
            i += 1
        i += 1
        word = ""
        while code[i] != "]":
            word += code[i]
            i += 1
        ind = var.index(word)
        i += 1
        while code[i] == " ":
            i += 1
        word = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                word += code[i]                 
                i += 1
            word = val[ind]
        else:
            while code[i] != "\n":
                word += code[i]
                i += 1
            word = int(word)
        val[ind] = stack[word-1]

    elif word == "RAK":
        os.system("clear")

    elif word == "URI":
        i += 1
        while code[i] == " ":
            i += 1
        word = ""
        if code[i] == "[":
            i += 1
            while code[i] != "]":
                word += code[i]                 
                i += 1
            word = val[ind]
        else:
            while code[i] != "\n":
                word += code[i]
                i += 1
            word = int(word)
        time.sleep(word/1000)

    elif word == "VER":
        while code[i] != "(":
            i += 1
        i += 1
        word = ""
        while code[i] != ")":
            word += code[i]
            i += 1
        fname.append(word)
        i += 1
        word = ""
        while code[i] != "!":
            word += code[i]
            i += 1
        fcont.append(word)

    elif word == "STE":
        while code[i] != "(":
            i += 1
        i += 1
        word = ""
        while code[i] != ")":
            word += code[i]
            i += 1
        ind = fname.index(word)
        word = fcont[ind]
        i += 2
        code = code[:i] + word + code[i:]                   

    elif word == "/":
        i += 1
        while code[i] != "/":
            i += 1     
    
    elif word == "DAK":
        break
    
        
    i += 1

