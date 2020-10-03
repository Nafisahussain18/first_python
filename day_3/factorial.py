fact = 1
n = eval(input('find the factorial of :'))
for i in range(n, 1, -1):
    fact = fact*i

print(f'The {n}! = {fact}')
