#User function Template for python3
import math

def nearestPower(a,b):
    ##Your code here
    ##return the closest power
    x=math.floor(math.log(b,a))
    xPlusOne=x+1
    number1=a**x
    number2=a**xPlusOne
    if(abs(number1-b)>abs(number2-b)):
        return number2
    else:
        return number1
