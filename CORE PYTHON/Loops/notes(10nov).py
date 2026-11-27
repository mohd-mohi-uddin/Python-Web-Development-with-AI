num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

operator = input("enter the operator: ")

match operator:
    case "+":
        a = num1 + num2
        print("addition of two numbers:",a)
    case "-":
        a = num1 - num2
        print("subtraction of two numbers:",a)
    case "*":
        a = num1 * num2
        print("multiplication of two numbers:",a)
    case "/":
        a = num1 / num2
        print("division of two numbers:",a)
    case _:
        print("invalid choice")