if __name__ == '__main__':
    s = input().strip()
    for i in s:
        if i.isalnum()== True:
            print(True) #  check whether the string has alphanumeric characters
            break
    for i in s:
        if i.isalpha()== True:
            print(True) # check whether the string has alphabetical characters
            break
    for i in s:
        if i.isdigit()== True:
            print(True) # check whether the string has digit characters
            break
    for i in s:
        if i.islower()== True:
            print(True) # check whether the string has lowercase characters
            break
    for i in s:
        if i.isupper()== True:
            print(True) # check whether the string has uppercase characters
            break
    
    # single method checks all the characters in the string if any one of them satisfies the condition it returns True
    # so we use loop to iterate through each character to check whether the one character is satisfying the condition or not