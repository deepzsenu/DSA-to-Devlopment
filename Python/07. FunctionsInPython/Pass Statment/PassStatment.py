
'''
Pass Statement
The pass statement is a null statement. But the difference between pass and comment
 is that comment is ignored by the interpreter whereas pass is not ignored.

The pass statement is generally used as a placeholder i.e. when the user does 
not know what code to write. So user simply places pass at that line. Sometimes, 
pass is used when the user doesn’t want any code to execute. So user can simply place
pass where empty code is not allowed, like in loops, function definitions, class definitions,
or in if statements. So using pass statement user avoids this error.

Syntax:

pass

Example 1: Pass statement can be used in empty functions

def geekFunction:
      pass
Example 2: pass statement can also be used in empty class

class geekClass:
     pass
Example 3: pass statement can be used in for loop when user doesn’t know what to code inside
 the loop
'''
n = 10
for i in range(n):
     # pass can be used as placeholder
     # when code is to added later
     pass
'''
Example 4: pass statement can be used with conditional statements
'''
a = 10
b = 20
 
if a > b:
    pass 
else:
    print("b")  # This will be printed since a is not greater than b
'''
Example 5: lets take another example in which the pass statement get executed when the
 condition
is true
'''
li =['a', 'b', 'c', 'd']
 
for i in li:
    if(i =='a'):
        pass
    else:
        print(i)
'''
Output:

b
c
d
'''