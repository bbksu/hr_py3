def print_rangoli(size):
    # your code goes here
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]    
    
    
    length = (size - 1)*2
    length = length + length+1
    print(length)
    
    letters = "-".join(alphabet[:size])
    print(letters)
    # for i in range(size):
    #     letters += f"{alphabet[i]}-"
    #     print(length*"-")    

    
    
if __name__ == '__main__':
    # n = int(input())
    n = 3
    print_rangoli(n)