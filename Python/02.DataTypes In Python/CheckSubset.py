'''
Check Subset
Difficulty: EasyAccuracy: 79.54%Submissions: 4K+Points: 2
Given two sets a and b. check whether a is subset of b ?

a is subset of b, if all elements of a set a are present in another set b.

Examples:

Input: a = [1, 4, 3], b = [1, 4, 3, 2]
Output: True

'''

a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

########### Write your code below ###############
res = a.issubset(b)

########### Write your code above ###############
# Print True or False
print(res)


# Method 2

a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

########### Write your code below ###############
res = all(elem in b for elem in a)
########### Write your code above ###############

print(res)

