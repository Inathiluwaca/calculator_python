


def user_digit():
    while True:
        try:
            num1= int(input("Insert the first digit.\n"))
            num2= int(input("Insert the second digit.\n"))
            return num1,num2
        except ValueError:
            print("Error: Insert a number.")

            
def instructions():
    print("INSTRUCTIONS:\n")
    explanations = "Addition : +\nSubraction : -\nMultiplication : *\nDivision : /\nExponential : **\nRemainder : %\n"
    print(explanations)


def user_operator():
    user_sign= ["+","-","*","/","**","%"]
    while True:
        user_choice= input("Insert the operator you want to use.\n")
        if user_choice not in user_sign:
            print("Error: Insert valid operator.")
        else:
            return user_choice
        

def addition(num1,num2):
    addition = num1+ num2
    print(addition)


def subtraction(num1,num2):
    subtract= num1-num2
    print(subtract)


def multiplication(num1,num2):
    multiply= num1*num2
    print(multiply)


def division(num1,num2):
    divide = num1/num2
    print(divide)


def exponential(num1,num2):
    exponent= num1 ** num2
    print(exponent)

def remainder(num1,num2):
    remain= num1%num2
    print(remain)


def run_sums(operator,num1,num2):
    
    if operator == "+":
        addition(num1,num2)
    elif operator == "-":
        subtraction(num1,num2)
    elif operator == "/":
        division(num1,num2)
    elif operator == "**":
        exponential(num1,num2)
    elif operator == "%":
        remainder(num1,num2)

if __name__ == "__main__":
    while True:
        num1,num2=user_digit()
        instructions()
        operator=user_operator()
        run_sums(operator,num1,num2)
        progress= input("Do you want to do more sums? Insert Yes or No.\n").lower()
        if progress == "yes":
            print("Welcome back.")
        else:
            print("Goodbye.")
            break
