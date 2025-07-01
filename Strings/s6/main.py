import textwrap

def wrap(string, max_width):    
    word_wrap = textwrap.TextWrapper(width=max_width)
    string_list = word_wrap.wrap(string)
    wst = ""        
    for i in string_list:
        wst += i+"\n"
    return wst[:-1]

if __name__ == '__main__':
    #string, max_width = input(), int(input())
    string, max_width = "ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4
    result = wrap(string, max_width)
    print(result)    
    