#Ans 1:

tuple1 = (2,4,5,6,2,3,4,4,7)
count = 0

for i in tuple1:
    if i == 4:
        count += 1

print(count)

#Ans 2:

listx = [5,10,7,4,15,3]

tup2 = tuple(listx)

print(tup2, type(tup2))

#Ans 3:

tuples_list = [(1,2),(3,4),(5,6)]

sum_of_tuples = []
for i in tuples_list:
    ans = sum(i)
    sum_of_tuples.append(ans)
sum_of_list = sum(sum_of_tuples)

print(sum_of_list)

#ans 4

employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

employees = (employee1, employee2, employee3)

print("Employee Records:")

for employee in employees:
    name, emp_id, department, salary = employee

    print("Name:", name)
    print("Employee ID:", emp_id)
    print("Department:", department)
    print("Salary: $", salary)