row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?(type in the form of 'row column':")
user_input = position.split(" ")
row = int(user_input[0])
column = int(user_input[1])
map[column-1][row-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")
