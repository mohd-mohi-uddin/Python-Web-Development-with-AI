set1 = {1,2,3,"apple",22.5}

s1 ={11,11,22,22,33,33}
print(s1)

#output = {33,11,22}




s2 = set()
print(type(s2))

#use set constructor to make empty set because the empty curly braces will give you a dictionary.





# print(s1+set1)

#it does not support the concatination




print(1 in set1)

#we can use member ship operators 




#create a list and convert in set
listx = [1,2,3,3,4,5]
setx = set(listx)
print(setx)



#len
print(len(setx))



#add
#use add to add a element in the index

setx.add(100)
print(setx)



#remove
setx.remove(100)
print(setx)



#discard
setx.discard(5)
print(setx)

#discard will not throw a error if you give a wrong value.



#pop
setx.pop()
print(setx)



'''clear'''
# setx.clear()
# print(setx)




setx= list(setx)
i = 0
while i < len(setx):
    print(setx[i])
    i += 1




s3 = {2,3,4,5,6,7}
s4 = {5,7,8,9,10}

#union
print(s3.union(s4))
print(s3|s4)



#intersection
print(s3.intersection(s4))
print(s3&s4)



#difference
print(s3.difference(s4))
print(s3-s4)



#symmetruc_differnce
print(s3.symmetric_difference(s4))
print(s3^s4)



#intersection_update
print(s3.intersection_update(s4))
print(s3)