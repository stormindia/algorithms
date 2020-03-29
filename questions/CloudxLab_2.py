# Problem 2 solution(Python 3):
# You are given a CSV file employees.csv as shown below. In this file,  the managerid column refers to the id of the employee who is a manager. So, the manager is also an employee. For example Ramesh is the manager of Dinesh in the CSV file given below.
#
# employees.csv
#
# Id, name, managerid
# 1, Dinesh, 2
# 2, Ramesh, 4
# 3, Sandeep, 4
# 4, Abhishek, NULL
#
# You have to read this csv file and create a tree like structure in which parent node is the manager of the child node. You can use “\t” tab for indentation or showing the hierarchy.
#
# Output for the above file -
#
# Abhishek - 4
# 	Ramesh - 2
# 		Dinesh - 1
# 	Sandeep - 3
#
# Please comment your code properly so that we can understand your approach.

#This code also works for the case where there are more than 1 managers who don't have report to anyone
#So in addition to above mentioned inputs, below inputs also work -
#Input
# Id, name, managerid
# 1, Dinesh,	2
# 2, Ramesh,	4
# 3, Sandeep,	4
# 4, Abhishek,	 NULL
# 5,  Abhek,	 NULL

#Output
# Abhishek - 4
# 	Ramesh - 2
# 		Dinesh - 1
# 	Sandeep - 3
# Abhek - 4


#below code will also work if an employee has more than 1 manager
#however, we need to assume that the manager's row number in the CSV must be same as that of ID as displayed in the sample inputs (!important)
#otherwise we would need to perform a search in the entire data
#Input
# Id, name, managerid
# 1, Dinesh,	2
# 2, Ramesh,	4
# 3, Sandeep,	4
# 4, Abhishek,	 NULL
# 5, Abhek,	 NULL
#6, asdasd, NULL
# 1, Dinesh,	6
# 3, Sandeep,	5

#Output
# Abhishek - 4
# 	Ramesh - 2
# 		Dinesh - 1
# 	Sandeep - 3
# Abhek - 4
# 	Sandeep - 3
# asdasd - 6
#   Dinesh - 1


import csv

employee_data = []  #list to store employee data
head_manager_index = [] #list to store head managers

with open('employees.csv') as f:
    data = csv.reader(f)
    for row in data:
        if(row[2] == ' NULL'):
            head_manager_index.append(int(row[0]) - 1)
            employee_data.append([int(row[0]), row[1].strip(), 'NULL', []]) #appending an empty list at last place here to store employees under current employee
        else:
            employee_data.append([int(row[0]), row[1].strip(), int(row[2].strip()), []])


#print(employee_data)

#appends the employees under the current employee
for i in range(len(employee_data)):
#appends the employees under the current employee
    if(employee_data[i][2] is not 'NULL'):
        managerid = employee_data[i][2] - 1
        employee_data[managerid][3].append(i)

#print(employee_data)

#Recusive function to print the data
def print_data(curr_index,curr_level):
    #printing required number of tabs
    for i in range(curr_level):
        print('\t', end='')

    print('{} - {}'.format(employee_data[curr_index][1], employee_data[curr_index][0]))

    for i in range(len(employee_data[curr_index][3])):
        #recursively printing data for all the employees
        print_data(employee_data[curr_index][3][i], curr_level + 1)

#Driver code to start the program
#For each head_manager print all the employees under him recursively
for i in head_manager_index:
    print_data(i, 0)
