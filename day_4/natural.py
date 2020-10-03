def sum_of_natural(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum


if __name__ == "__main__":
    x = eval(input(f'How many natural numbers you want to find the sum '))
    print(sum_of_natural(x))
