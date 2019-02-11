def main():
    n = int(input("Enter a number")) #number of inputs
    inputs = []
    for x in range(n):
        newline = input() #next input
        newline = newline.lower() #convert to lowercase
        newline = newline.strip() #trim
        inputs.append(newline) #add to list
    print(inputs)
    for i in range(n):
        w = dfa(inputs[i],int(i))
        if w == 0:
            print(str(i) + ', NO')
        if w == 1:
            print(str(i) + ', EMAIL')
        if w == 2:
            print(str(i) + ', WEB')

def dfa(input, n):
    s = input #stores string backup

    what = 0 #0 for NO, 1 for EMAIL, 2 for WEB

    nope = False #literally what it says

    #.count and @count
    dotC = 0
    atrC = 0

    for i in s:
        if ((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57) or ord(i) == 64 or ord(
            i) == 46): #a-z or 0-9 or @ or .

            if i == '@':
                atrC = atrC + 1

            if i == '.':
                dotC = dotC+1

        else:
            nope = True

    if s[0] == 'w' and s[1] == 'w' and s[2] == 'w' and s[3] == "." and dotC == 2:
        what = 2

    if atrC == 1 and dotC > 0:
        what = 1

    if atrC > 1:
        what = 0

    if dotC == 0:
        what = 0

    if nope == True:
        what = 0

    return what

if __name__ == "__main__":
    main()