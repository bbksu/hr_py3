# 1 4
# x**3 + x**2 + x + 1

x, k = input().split()
polynomial = input().replace("x", x)

if eval(polynomial) == int(k):
    print(True)
else:
    print(False)

