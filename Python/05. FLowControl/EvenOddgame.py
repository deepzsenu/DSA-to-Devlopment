'''
Even Odd Game
Difficulty: EasyAccuracy: 78.99%Submissions: 5K+Points: 2
Given a number n, number of apples in a bag. You and your friend are picking one apple turnwise from the bag. It is given that the first attempt is always by you. The person picking the last apple will be the winner. 

If you will win: print "You" (without quotes)
If your friend will win: print "Friend" (without quotes)
Examples:

Input: n = 9
Output: You
Input: n = 4
Output: Friend
Constraints:
1 <= n <= 100
'''

#User function Template for python3
# Take n input and print who wins

n = int(input())

if n%2 ==1:
    print("You")
else:
    print("Friend")