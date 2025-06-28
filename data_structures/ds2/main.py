if __name__ == '__main__':
    names = dict()
    scores = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        names.update({name: score})

    names = dict(sorted(names.items(), key=lambda x: x[0]))
    f_score = sorted(set(scores))[1]
    for i in names.items():
        if i[1] == f_score:
            print(i[0])
