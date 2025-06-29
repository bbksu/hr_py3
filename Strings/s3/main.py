from itertools import groupby

s = input()

s_group = groupby(s)
letters = dict()
for i, y in s_group:
    letters[i] = letters.setdefault(i, 0) + len(list(y))

occ = sorted(set(letters.values()), reverse=True)[:3]
letters = dict(sorted(letters.items(), key=lambda x: x[0]))

count = 0
for i in occ:
    for x, y in letters.items():
        if y == i:
            print(x, y)
            count += 1
        if count == 3:
            break
