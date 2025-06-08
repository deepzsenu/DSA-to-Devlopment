'''
Check Prime
Difficulty: EasyAccuracy: 38.32%Submissions: 6K+Points: 2Average Time: -1m
Given an integer n check if n is prime or not.
A prime number is a number that is divisible by 1 and itself only.

Note: Print "True" if n is prime, otherwise print "False".

Examples:

Input: n = 17
Output: True 
Explanation: 17 is  divisible by only 1 and 17. So it's a prime number.
Input: n = 56
Output: False
Explanation: 56 is divisible by 2, 4, 7.....etc. So its not a prime number.
Contraints:
1 <= n <= 104'''
#User function Template for python3
n = int(input())

if n <= 1:
    print(False)
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(False)
            break
    else:
        print(True)


# Approach 2

#User function Template for python3
n = int(input())

# Your code here
if n<=1:
    print(False)

elif n <=3:
    print(True)

elif n%2 == 0 or n%3 ==0:
    print(False)

else:
    i = 5 
    
    while ( (i*i) <= n):
        if n%i ==0 or n%(i+2) == 0:
            print(False)
            break
        i+=6
    else:
        print(True)
