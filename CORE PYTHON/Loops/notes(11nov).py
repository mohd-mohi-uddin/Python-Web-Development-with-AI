#CONTINUE

# for i in range(1,10):
#     if i == 3:
#         continue
#     print(i)

#BREAK

# for i in range(1,10):
#     if i == 3:
#         break
#     print(i)

#PASS

# for i in range(1,10):
#     if i == 3:
#         pass
#     print(i)

#Nested loops

# for i in range(5):
#     for j in range(5):
#         print("*")

#WHILE INSIDE WHILE:

# i = 0
# while i <= 2:
#     print("outer while")
#     i+=1
#     j = 0
#     while j <=2:
#         print("inner while")
#         j+=1

#FOR INSIDE WHILE:

# i = 0
# while i <= 2:
#     print("outer while")
#     i+=1
#     for i in range(3):
#         print("inner for")

#WHILE INSIDE FOR:

# for i in range(3):
#     print("OUTER for")
#     j = 0
#     while j <= 2:
#         print("inner while")
#         j += 1





#tables

# i = int(input("enter a number: "))
# a = i
# for j in range(10):
#     print(f"5 x {j+1} = {i}")
#     i += a





#sum of natural number:

'''homework'''
# total = 0
# num = 10
# for i in range(0,num+1):
#     total += i

# print(total)

# c = input("enter a number: ")
# count = 0
# for i in c:
#     count += 1
# print(count)





# factorail of a given number:

# c = int(input())
# factorials_of_values = 1

# '''homework'''
# for i in range(c,0,-1):
#     print(i)
#     factorials_of_values *= i

# print(factorials_of_values)


# num = int(input("Enter a number: "))

# fact = 1
# i = 1

# while i <= num:
#     fact = fact * i
#     i += 1

# print("Factorial:", fact)



#reversal of a number:

# c = int(input())

# for i in range(c,0,-1):
#     print(i)




'''homework'''
#reversal using while:


# num = int(input("Enter a number: "))
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# print("Reversed number:", rev)




#Palindronme

# num = int(input("Enter a number: "))

# temp = num
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")






#fibonacci series:

# n = int(input("enter a number: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c





#prime number:

# n = int(input())

# if n <= 1:
#     print("not a prime")

# for i in range(2,n):
#     if n % i == 0:
#         print("not a prime")
#         break
#     else:
#         print("prime")
#         break





total = 0

while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break

    total = total + num

print("Sum of numbers:", total)
