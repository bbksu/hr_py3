from itertools import combinations

string, length = input().split()
length = int(length)
combs = ""
for i in range(length+1):    
    string = sorted(string)
    perms = combinations(string, i)
    perms = map("".join, perms)
    perms = list(perms)
    perms.sort()    
    for i in perms:
        combs += f"{i}\n"

print(combs[1:-1])