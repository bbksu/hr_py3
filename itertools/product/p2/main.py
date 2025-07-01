from itertools import permutations

string, length = input(), int(input())
# string, length = "HACK", 2

perms = permutations(string, length)
perms = map("".join, perms)
perms = list(perms)
perms.sort()
for i in perms:
    print(i)
