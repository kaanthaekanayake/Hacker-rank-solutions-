if __name__ == '__main__':
    s = input().strip()
    
    #check whether the string has alphanumeric characters
    print(any(c.isalnum() for c in s))
    #check whether the string has alpha characters
    print(any(c.isalpha() for c in s))
    #check whether the string has digits
    print(any(c.isdigit() for c in s))
    #check whether the string has lowercase characters
    print(any(c.islower() for c in s))
    #check whether the string has uppercase characters
    print(any(c.isupper() for c in s))

# if there is one character the generator expression will return true.