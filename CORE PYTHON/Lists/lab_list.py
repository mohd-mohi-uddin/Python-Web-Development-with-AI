'''
1. Write a Python program to sum all the items in a list.

2. Write a Python program to get the largest and smallest number from a list without built-in functions.

3. Write a Python program to find duplicate values from a list and display those.

4. Write a Python program to split a given list into two parts where the length of the first part of the list is given.

5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
'''

#ans 1:

nums = [1,2,3,4,5,6,7]
added = 0
for i in nums:
    added += i
print(added)

#ans 2:

nums = [0,1,2,3,4,5,6,7]
max =0
min =0
for i in nums:
    if i > max:
        max = i
    if i < min:
        min = i

print(max,min)

#ans 3:

numbers = [1,2,1,3,2,4]

seen = []

for num in numbers:
    if num in seen:
        print(num)
    else:
        seen.append(num)

#ans 4:

my_list = [1, 1, 2, 3, 4, 4, 5, 1]

n = 3

first_part = my_list[:n]
second_part = my_list[n:]

print((first_part, second_part))

#ans 5:

my_list = ['red', 'green', 'white', 'black']

for i in range(len(my_list)-1, -1, -1):
    print(my_list[i])



