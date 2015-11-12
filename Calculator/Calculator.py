##
#  Functions
##
def summa(a, b):
    return a + b 


def deduction(a, b):
    return a - b


def multiplication(a, b):
    return a * b 


def division(a, b):
    result = None

    if y == 0:
        result = 'you tried to divide by zero'
    else:
        result = a / b

    return result

print("Enter x : ")
x = input()
x = int(x)

print("Enter y : ")
y = input()
y = int(y)

print("x = " + str(x))
print("y = " + str(y))


print("Choose operator: ")
print("1) +")
print("2) -")
print("3) *")
print("4) /")
choice = input()

##
#   Using functions
##

if choice == '1':
   result = summa(x, y) 
   print("x + y = " + str(result))


if choice == '2':
    result = deduction(x, y)
    print("x - y = " + str(result))

if choice == '3':
    result = multiplication(x, y)
    print("x * y = " + str(result))


if choice == '4':
    result = division(x, y)
    print("x / y = " + str(result))