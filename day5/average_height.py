student_height = input("Write the heights of students seperated by a space:").split(" ")
n = 0
sum_height = 0
for height in student_height:
    sum_height += int(height)
    n += 1
print(sum_height)
print(n)    


