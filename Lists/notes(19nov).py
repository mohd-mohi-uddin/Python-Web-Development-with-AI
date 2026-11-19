#a list is hetrogeneous means it can store multiple typle of vlaues

#[1,2,3],["apple","banana","mango"]


# list methods:

nums = []
nums = list((1,2,3,4,5))
nums.append(20)


#extend

nums.extend([30,40])

#pop

x = nums.pop()
print(x)

#reverse

nums.reverse()
print(nums)

#sort

nums.sort()
print(nums)

#count

count = nums.count(1)
print(count)


#list built in function

# len(nums)
# max(nums)
# min(nums)
# sum(nums)
# sorted(nums)
# reversed(nums)
# print(list(enumerate(nums)))

count = 0 
while count < len(nums):
    print(nums[count])
    count+=1
