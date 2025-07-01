def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        substring = string[i:i + len(sub_string)]
        if substring == sub_string:
            count += 1
    return count
