def logo(standard):    
    length = standard * standard    
    letter = "H"
    extends = (standard + 1) // 2
    print(extends)
    mid_range = (length+1) // 2
    mid_range = mid_range - (extends-1)//2
    mid_range = list(range(mid_range, mid_range+ extends))
    
    tip = ""
    shift = standard * 2    
    for i in range(1, (standard)*2, 2):
        letters = letter*i        
        spaces = length - standard
        tip += f"{letters:^{extends+standard+1}}{spaces * ' '}\n"        
    
    tip = tip[:-1]
    print(tip)    

    for i in range(standard+1, (length-standard)+1):
        space = (length - (standard*2) - extends)        
        letters = letter * standard        
        if i in mid_range:
            print(f"{(letters*standard):^{length + standard}}")
            continue
        print(f"{letters:^{shift}}{space*' '}{letters}")
    print(tip[::-1])

if __name__ == '__main__':
    logo(int(input()))