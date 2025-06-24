_ = input(" ")
t_array = input(" ").split(" ")
a = input(" ").split(" ")
b = input(" ").split(" ")


a_b = set(a+b)
a = set(a)
b = set(b)
f_set = ((a_b & set(t_array)) ^ a & b)

n_array = list()
for i in t_array:
    if i in f_set:
        n_array.append(i)        


d_array = dict()
for i in n_array:
    d_array[i] = d_array.setdefault(i, 0) +1

for i in b:
    d_array[i] = d_array.get(i, 0) *-1

print(sum(d_array.values()))