def minion_game(string):
    # your code goes here
    letters = set(string)
    vowels = {"A", "E", "I", "O", "U"}
    kevin = vowels & letters
    k_dict = points_dict(string, kevin)
    kevin_score = f_score(k_dict, string)

    stuart = (vowels ^ letters) & letters
    s_dict = points_dict(string, stuart)
    stuart_score = f_score(s_dict, string)

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print(f"Stuart {stuart_score}")



def f_score(s_dict, string):
    score = 0
    print(s_dict)
    for i in s_dict.keys():
        score += string.count(i)

    return score


def points_dict(string, name):
    l_dict = dict()
    for i in name:
        s_index = string.index(i)
        for y in range(len(string) + 1):
            e_string = string[s_index:s_index + y]
            l_dict.update({e_string: 0})
    print(l_dict)
    l_dict.pop("")
    return l_dict


if __name__ == '__main__':
    S = input()
    minion_game(S)
