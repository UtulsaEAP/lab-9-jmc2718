def fibonacci(n):
    if n < 0:
        f2 = -1
        return f2
    elif n == 0:
        f2 = 0
        return f2
    f1 = 1
    f2 = 1
    n = n-2
    while n > 0:
        f2 = f1 + f2
        f1 = f2 - f1
        n = n - 1
    #write your code here
    return f2

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')