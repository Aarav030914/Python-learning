with open("./day26/file1.txt") as file1:
    content1 = file1.read()
with open("./day26/file2.txt") as file2:
    content2 = file2.read()
content1_list = content1.split()
content2_list = content2.split()
result = [int(num) for num in content1_list if num in content2_list]

# Write your code above 👆

print(result)


