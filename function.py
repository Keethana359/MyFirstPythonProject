# method 1
def find_add(n1,n2):
    n3=n1+n2
    return n3
print(find_add(10,20))

def find_sub(n1,n2):
    n3=n1-n2
    return n3
print(find_sub(10,20))
def find_mul(n1,n2):
    n3=n1*n2
    return n3
print(find_mul(10,20))
def find_div(n1,n2):
    n3=n1/n2
    return n3
print(find_div(10,20))


#  method 2
def add(n1,n2):
    print(n1+n2)
add(10,20)

def sub(n1,n2):
    print(n1-n2)
sub(10,20)

def multiple(n1,n2):
    print(n1*n2)
multiple(10,20)

def div(n1,n2):
    print(n1/n2)
div(10,20)

# method 3
def mul(a,b):
    return a*b

print("multiplcation:",mul(10,40))

def div(a,b):
    if b != 0:
        return a/b
    else:
        return "cannot divided by zero"

# get user input
a=float(input('enter the a number'))
b=float(input('enter the b number'))

print("division:",div(a,b))