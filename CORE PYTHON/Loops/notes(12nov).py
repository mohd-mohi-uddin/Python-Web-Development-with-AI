#functions

# def div(a,b):
#     print(a/b)

# div(2,3)

#return and variable saving:

# def add(a,b):
#     return a+b

# sum_of_ab = add(3,5)
# print(sum_of_ab)

#return multiple vslues:

# def calculate(a,b):
#     add = a+b
#     sub = a-b
#     mul = a*b
#     return add,sub,mul

# x,y,z = calculate(2,3)
# print(x,y,z)
# print(z,y,x)
# print(x)

#square:

# def square(a):
#     return a**2

# print(square(3))




#lambda

add = lambda a,b:a+b
print(add(2,3))

even = lambda n: "even" if n % 2 == 0 else "odd"
print(even(5))