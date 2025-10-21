n = int(input("Enter num of Students : "))

records = {} # Dictionary to store name and the score list

# read n number of lines with "name score1 score2 .."
for i in range (n):
    parts = input().split() #split the line to tokens from the white spaces
    name = parts[0] # First token is the student name
    scores = list(map(float,parts[1:])) # rest of the list items are scores and convert them in to floats
    records[name] = scores # store name and the scores as key:value pair in a dictionary

#find the average of the relavent name's score list
query_name = input().strip()  # get the name and remove unnesssary white spaces and /n characters
#input already with a /n- new line character it remove using strip
student_scores = records[query_name] # get the score relavent to the given name as input
average = sum(student_scores)/len(student_scores) # find the average
print("{:.2f}".format(average)) # print the average with two decimal places
