##
#  Functions
##
def convertable_to_int(a):
    try:
        int(a)
        return True
    except:
        return False


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

def square(a):
    return a * a 

choice = None
result = None

while choice != '0':
    x = None
    while type (x).__name__ != 'int':
        print("Enter x : ")
        x = input()
        if convertable_to_int(x) == True:
            x = int(x)
        
    y = None 
    print("Choose operator: ")
    print("0) exit")
    print("1) +")
    print("2) -")
    print("3) *")
    print("4) /")
    print("5) sqr")
    choice = input()


    operator = None


    ##
    #   Using functions
    ##
    if choice == '1' or choice == '+':
        operator = '+'
        result = summa(x, y) 

    if choice == '2' or choice == '-':
        operator = '-'
        result = deduction(x, y)

    if choice == '3' or choice == '*':
        operator = '*'
        result = multiplication(x, y)

    if choice == '4' or choice == '/':
        operator = '/'
        result = division(x, y)

    if choice == '5'or choice == '*':
        operator = '*'
        result = True

    if operator == None or result == None:
        print('Are you sure? [Yes|No]')
        sure = input() # sure => 'Y'
        sure = sure.lower() # sure => 'y'

        if sure == 'y' or sure == 'yes': # 'y' != 'Y'
            print('Bye!!')
        elif sure == 'n' or sure == 'no':
            choice = None 
    else:
        if choice == '5' or 'square':
            x_square = square(x)
            y_square = square(y)
            print("x " + str(operator) + " x = " + str (x_square))
            print("y " + str(operator) + " y = " + str (y_square))
        else:
            print("x " + str(operator) + " y = " + str(result))