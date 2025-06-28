if __name__ == '__main__':
    x = input()
    y = input()
    z = input()
    n = input()

    perm_list = []
    for i in range(x + 1):
        for y in range(y + 1):
            for a in range(z + 1):
                perms = [i, y, a]
                if n != sum((i, y, a)):
                    perm_list.append(perms)
    print(perm_list)
