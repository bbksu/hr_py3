if __name__ == '__main__':
    N = int(input())
    lst = list()
    for i in range(N):
        run = input().strip().split()
        command = run[0]
        if command == "insert":
            lst.insert(int(run[1]), int(run[2]))
        elif command == "print":
            print(lst)
        elif command == "remove":
            lst.remove(int(run[1]))
        elif command == "append":
            lst.append(int(run[1]))
        elif command == "sort":
            lst.sort()
        elif command == "pop":
            lst.pop(-1)
        else:
            lst.reverse()
