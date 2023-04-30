
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

#Below we extrapolate which row (row1,row2,row3) We edit and define a new var

selected_row = map[vertical - 1]

#Then, within the row, we then look at which string in the array we have to change to X

selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
