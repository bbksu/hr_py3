def word_order(words):
    output = f"{str(len(set(words)))}\n"
    l_l = dict()
    for w in words:
        l_l[w] = l_l.setdefault(w, 0) + 1

    output += str(list(l_l.values())).replace("[", "").replace("]", "").replace(",", "")
    print(output)


if __name__ == '__main__':
    inputs = []
    n = int(input())
    for i in range(n):
        inputs.append(input())

    word_order(inputs)
