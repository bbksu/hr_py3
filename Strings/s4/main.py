def merge_the_tools(merge_string, k):
    count = 0
    out = dict()
    merge = ""
    for i in merge_string:
        out[i] = out.setdefault(i, 0)+1
        if count == k -1:
            count = 0
            merge += f"{list(out.keys())}\n"
            out.clear()
            merge_string = merge_string[3:]
            continue
        count += 1
    merge += f"{list(out.keys())}"
    merge = swap(merge)[:-1]

    print(merge)

def swap(string):
    items = "[], '"
    for i in items:
        string = string.replace(i, "")
    return string


if __name__ == '__main__':
    string, k = input(), int(input())

    merge_the_tools(string, k)
