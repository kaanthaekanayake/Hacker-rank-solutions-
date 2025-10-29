# Convert lower case letters to uppser case vise versa.
def swap_case(s):
    swaped_string = [] # use to add letters after change its case

    for L in s:
        if L.islower(): # check whether the letter is lower case
            swaped_string.append(L.upper()) # convert lower to upper
        elif L.isupper(): # check whether the letter is upper case
            swaped_string.append(L.lower()) # convert upper to lower
        else:
            swaped_string.append(L)
    return "".join(swaped_string) # Join above array's letters to a single string

if __name__ == '__main__':
    s = input().strip()
    result = swap_case(s)
    print(result)

    # You can do this whole thing with a single line (below)
    # print(input().strip().swapcase())