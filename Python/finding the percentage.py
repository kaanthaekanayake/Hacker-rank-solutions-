n = int(input("Enter num of Students : "))

records = {}

for i in range (n):
    parts = input().split()
    name = parts[0]
    scores = list(map(float,parts[1:]))
    records[name] = scores

query_name = input().strip()
student_scores = records[query_name]
average = sum(student_scores)/len(student_scores)
print("{:.2f}".format(average))
