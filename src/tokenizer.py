from typing import List, Any
import re
import sys
keylist = ''
synt = [',','.','(',')','[',']','{','}',':',';']

keys = []
iden = []
mOp = []
lOp = []
numV = []
others = []

def token(s):
    str1 = s.split(' ')
    i = 0
    j = len(str1)
    while(i<j):
        try:
            float(str1[i])
            numV.append(str1[i])
        except ValueError:
            print()

        if str1[i] in keylist:
            if str1[i] not in keys:
                keys.append(str1[i])
        if str1[i] == '+' or str1[i] == '-' or str1[i] == '*' or str1[i] == '/' or str1[i] == '=':
            if str1[i] not in mOp:
                mOp.append(str1[i])
        if str1[i] == '|' or str1[i] == '&' or str1[i] == '!=' or str1[i] == '==' or str1[i] == '>' or str1[i] == '<' or str1[i] == '>=' or str1[i] == '<=':
            if str1[i] not in lOp:
                lOp.append(str1[i])
        if str1[i].isdigit():
            if str1[i] not in numV:
                numV.append(str1[i])
        if str1[i] in synt:
            if str1[i] not in others:
                others.append(str1[i])
        if str1[i].isidentifier():
            if str1[i] not in keylist:
                if str1[i] not in iden:
                    iden.append(str1[i])
        i = i + 1

def takein():
    global keylist
    f = open("keywords.txt", "r")

    if f.mode == 'r':
        keylist = f.read()
    keylist = keylist.split('\n')

    f = open("input.txt", "r")

    if f.mode == 'r':
        contents = f.read()
    contents = contents.split('\n')

    i = 0
    j = len(contents)
    while(i<j):
        contents[i] = contents[i].strip()
        i = i + 1
    return contents

def main():
    contents = takein()
    for x in contents:
        token(x)

    print('Keywords: ' + str(keys))
    print('Identifiers: ' + str(iden))
    print('Math Operators: ' + str(mOp))
    print('Logical Operators: ' + str(lOp))
    print('Numerical Values: ' + str(numV))
    print('Others: ' + str(others))


if __name__ == "__main__":
    main()
