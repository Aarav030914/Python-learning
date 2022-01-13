#Taking the string input of scores from the user 
student_scores = input("Input a list of student scores seperated by a space:").split()

#converting the string scores into integers
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

#finding the maximum of the scores
for i in range(1,len(student_scores)):
    max_score = student_scores[0]
    if max_score < student_scores[i]:
        max_score = student_scores[i]
    else:
        max_score = max_score
print(max_score)            

