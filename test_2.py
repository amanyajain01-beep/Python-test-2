def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b 
def divide(a,b):
    try: 
        return a/b 
    except ZeroDivisionError:
        return "Error: cannot be divided by zero"

def calculator():
    print("FUNCTION CALCULATOR")
    print("PLEASE SELECT AN OPERATION : ")
    print("1: ADD (+) ")
    print("2: SUBTRACT (-) ")
    print("3:MULTIPLY (*)")
    print("4: DIVID (/)")

    choice = input("ENTER CHOICE (1,2,3,4) : ")

    if choice in ['1','2','3','4'] :
        try:
            num1 = float(input("Enter first number"))
            num2 = float(input("Enter second number"))
            if choice == '1' :
                result = add(num1,num2)
            elif choice == '2':
                result = subtract(num1,num2)
            elif choice =='3':
                result = multiply(num1,num2)
            elif choice == '4' : 
                result = divide(num1,num2)

            print(f"RESULT : {result}")
        except ValueError :
            print("ERROR: INVALID INPUT! PLEASE ONLY ENTER NUMEBERS")
    else: 
        print("ERROR: CHOICE OF OPERATION IS INVALID.") 

calculator()