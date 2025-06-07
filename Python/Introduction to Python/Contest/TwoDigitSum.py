# Approch 1  naive method using strings
#User function Template for python3

def digitsSum(n):
    ##Your code here
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum

# Approach 2 using modulo

def digitsSum(N):
    ##Your code here
    
    sum = 0
    m = N
    
    while m>0:
        
        rem = m%10
        sum+=rem
        m = m//10
    
    return sum
        
