from itertools import combinations_with_replacement

string, length = input().split()
length = int(length)
combs = ""
string = sorted(string)
perms = combinations_with_replacement(string, length)
perms = map("".join, perms)
perms = list(perms)
perms.sort()    
for i in perms:
    combs += f"{i}\n"    

print(combs[:-1])