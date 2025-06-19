def compute(x, y):

    if x>y:
        smaller = y
    else:
        smaller = x
    
    for i in range(1,smaller+1):
        if((x%i ==0) and y%i ==0):
            ans  = i
    return ans

num1 = 54
num2 = 24
# print(compute(num1, num2))

print("abcefd".replace('cd','12'))


def f(value, values):
    v = 1
    values[0] = 44

a = 3
v = [1,2,3]

f(a, v)
print(a,v[0])