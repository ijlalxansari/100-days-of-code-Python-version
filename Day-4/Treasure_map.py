# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
row4 = ["⬜️", "⬜️", "⬜️"]

map = [row1, row2, row3, row4]
print(f"{row1}\n{row2}\n{row3}\n{row4}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

map[int(position[0])][int(position[1])] = 'X'

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}\n{row4}")
