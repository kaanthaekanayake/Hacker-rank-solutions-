def count_substring(string, sub_string):
    count = 0
    s = len(string) # get the length if main string
    sb = len(sub_string) # get the length of substring
    for i in range(0,s-sb+1): # iterate after 4th index in not usable so to stop that we substract the length of sub string
        get_slice = string[i:sb+i] # get the slice of main string from index i to length of substring + i
        if sub_string == get_slice: # compare the substring with the slice of main string
            count +=1 # increment the count if found
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)