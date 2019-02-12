import re

def regular(s, pat, m):
    fool = False
    for x in range(m):
        matchObj = re.match(pat[x], s)
        if matchObj:
            fool = True
            print("YES, " + str(x + 1))
            break
    if fool == False:
        print("NO, 0")



def main():

    f = open("pattern.txt", "r")

    if f.mode == 'r':
        patto = f.read()
    patto = patto.split('\n')

    n = int(patto[0])
    patto.remove(patto[0])

    f = open("string.txt", "r")

    if f.mode == 'r':
        string = f.read()
    string = string.split('\n')

    m = int(string[0])
    string.remove(string[0])

    print(patto)
    print(string)

    for x in range(m):
        regular(str(string[x]), patto, n)


if __name__ == "__main__":
    main()