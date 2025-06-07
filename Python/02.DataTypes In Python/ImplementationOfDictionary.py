'''
You are familiar with most of the properties of dictionaries in Python. Let's get this into head by solving a problem.
The task is to do operations as described below:

k key, v value: Insert given key k and value v in the dictionary, print 'Inserted' after inserting.
d key: Delete the entry for a given key d and print 'Deleted' if the key to be deleted is present, else print '-1'.
p key: Print marks of given key p in statement as "Marks of {student_name} is : {marks}". If key is not present print '-1'.
Avoid using F-string in your python solution code
Examples:

Input:
dhi ankit
100 200
harsh 300
harsh
harsh
Output:
Inserted
Deleted
-1
Explanation: First two lines take my_dict input as key and values. Then, insert and del 
operation happens, correspondingly Inserted and Deleted is printed. For last query, harsh 
key is not present so -1 is printed.
Input:
harsh ghutra mith
100 200 300
ankit 400
mith
ankit
Output:
Inserted
Deleted
Marks of ankit is 400
Explanation: First two lines take my_dict input as key and values. Then, insert and del
 operation happens, correspondingly Inserted and Deleted is printed. For last query, Marks 
 of ankit is 400 is printed.
 

Constraints:
1 <= | key | <= 20
1 <= marks <= 105
'''
# Taking input and initializing dictionary
keys = input().split()
values = map(int, input().split())
my_dict = dict(zip(keys, values))
k, v = input().split()

########### Write your code below ###############
# Insert k,v in my_dict
# Print Inserted if inserted successfuly
my_dict[k] = int(v)
print("Inserted")
########### Write your code above ###############

d = input()

########### Write your code below ###############
# Delete entry with key d from my_dict
# Print Deleted if deleted successfuly else print -1
if d in my_dict:
    del my_dict[d]
    print("Deleted")
else:
    print(-1)
########### Write your code above ###############

p = input()

########### Write your code below ###############
# Print marks of given key p if key present, else print -1
if p in my_dict:
    print("Marks of "+p+" is "+str(my_dict[p]))
else:
    print(-1)
    

########### Write your code above ###############