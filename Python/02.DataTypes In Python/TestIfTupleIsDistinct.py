'''
Test if tuple is distinct
Difficulty: EasyAccuracy: 50.0%Submissions: 18K+Points: 2Average Time: 10m
Given a tuple arr , print "True" if all elements of tuple are different otherwise print
 "False".

A tuple is a collection of items that are ordered and unchangeable.

Examples:

Input:
arr = (1, 2, 3, 4, 5, 4)
Output: False
Input:
arr = (1, 2, 3, 4, 5)
Output: True
'''

#User function Template for python3
arr = tuple(map(int, input().split()))

########### Write your code below ###############
# Print "True" if all elements of tuple are different, otherwise print "False"
if len(set(arr)) == len(arr):
    print(True)
else:
    print(False)
########### Write your code above ###############

