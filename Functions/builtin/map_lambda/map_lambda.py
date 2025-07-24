cube = lambda x: x**3# complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    count = 0
    start = 1
    sequence = []
    if n == 0:
        return []
    elif n == 1:
        sequence.append(count)
    elif n >= 2:
        sequence += [count, start]
        for i in range(n-2):
            number = count + start
            count = start
            start = number
            sequence.append(number)
    return sequence


if __name__ == '__main__':
    # n = int(input())
    n = 5
    print(list(map(cube, fibonacci(n))))


# fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
# cube = lambda x: x * x * x
# print(list(map(cube, map(fib, range(int(input()))))))