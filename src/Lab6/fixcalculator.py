class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Use peek to look at the top of the stack

    def peek(self):
	    return self.stack[0]

# Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()


def main():

    f = open("variables.txt", "r")

    if f.mode == 'r':
        var = f.read()
    var = var.split('\n')

    vardict = {}

    for x in var:
        variable = x.split('=')
        vardict[variable[0]] = variable[1]


    for x in vardict:
        print(x + " " + str(vardict[x]))

    f = open("input.txt", "r")

    if f.mode == 'r':
        inputs = f.read()
    inputs = inputs.split('\n')

    stacc = Stack()
    output = ''

    for x in inputs:
        for y in x:
            if y in keys:
                output = output + str(y)
            if y == '+':




if __name__ == "__main__":
    main()