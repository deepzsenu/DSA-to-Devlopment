'''
Next Prime Number
Difficulty: MediumAccuracy: 48.22%Submissions: 4K+Points: 4
Given an integer n. Write a program to find the first prime number greater than n.

Examples:

Input: n = 15
Output: 17
Explanation: 17 is next prime number.
Input: n = 7
Output: 11
Explanation: 11 is the prime number next to 7.
Constraints:
1 <= n <= 500
'''
#User function Template for python3
def checkPrime(n):
    if n<=1:
        return False

    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        else:
            return True

n = int(input())

# Your code here

while(checkPrime(n+1)== False):
    n+=1
print(n+1)
