# #1

# year = int(input("Enter a year: "))

# if year % 4 == 0:
#     print("It is a Leap Year")
# else:
#     print("It is not a Leap Year")




# #2


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest number is:", a)
# elif b >= a and b >= c:
#     print("Largest number is:", b)
# else:
#     print("Largest number is:", c)



# #3


# num = int(input("Enter a number: "))

# if num > 0:
#     print("The number is Positive")
# elif num < 0:
#     print("The number is Negative")
# else:
#     print("The number is Zero")


#4



code = int(input("Enter product code (1, 2, 3): "))
amount = float(input("Enter order amount: "))

discount = 0

match code:
    case 1:
        if amount > 1000:
            discount = amount * 0.10

    case 2:
        if amount > 100:
            discount = amount * 0.05

    case 3:
        if amount > 500:
            discount = amount * 0.10

    case _:
        print("Invalid product code")


net_amount = amount - discount

print("Order Amount:", amount)
print("Discount:", discount)
print("Net Amount:", net_amount)

