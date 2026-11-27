#Nested functions

# def outer():
#     print("outer")

#     def inner():
#         print("inner")
#     inner()

# outer()

def add(a,b):
    def square(n):
        return n*n
    return square(a) + square(b)

print(add(2,3))