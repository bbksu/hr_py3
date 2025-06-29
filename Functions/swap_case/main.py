def swap_case(s):
    string = ""
    for i in s:
        if i.isupper():
            i = i.lower()
        else:
            i = i.upper()
        string += i
    return string
