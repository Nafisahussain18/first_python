n1, n2, n3, n4, n5 = eval(input(f'inter the numbers :'))
# print(n1, n2, n3, n4, n5)
max = n1
if (n2 > max):
    max = n2

if (n3 > max):
    max = n3

if (n4 > max):
    max = n4

if(n5 > max):
    max = n5

print(f'The largest number is: {max}')
