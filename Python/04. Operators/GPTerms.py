'''
Geometric Progression Term
Difficulty: EasyAccuracy: 77.8%Submissions: 5K+Points: 2
Given three integers, a, r and n. Where a is the first term, r is the common ratio of a G.P. and r is equal to 2.  Calculate the nth term of GP.

The nth term is given by an = a * r(n-1), where r = 2.

Examples:

Input: a = 2, n = 10
Output: 1024
Explanation: an = a * rn-1 = 2 * 210-1 = 1024'''

#User function Template for python3
a = int(input())
n = int(input())
r = 2

########### Write your code below ###############
# Compute the GP Term
ans =  a *( r**(n-1))
########### Write your code above ###############

print(ans)
