a = "1 2 3 4 5 6 7 8 9".split()
b= "10 1 2 3 11 21 55 6 8".split()

a = set(a)
b = set(b)

print(a | b)

print(a.union(b))
