# get num of elements
n = int(input().strip()) # remove leading and trailing whitespaces and newline character
raw_data = map(int,input().split()) # Split input using the white spaces and add to a list

t = tuple(raw_data) # convert into a tuple - data type convertion
print(hash(tuple)) # Print hash