import pdb

def multification(a, b):
    return a * b    

pdb.set_trace()

x = input("Enter first number: ")
y = input("Enter second number: ")

mul = multification(int(x), int(y))
print(mul)


# we can use "pdb.set_trace()" or "breakpoint()" to set a breakpoint in the code.
# When the code execution reaches this line, it will pause and allow you to inspect variables,