print("TREASURE HUNT")


row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

place = input("Where do u want to put the treasure? (Specify in terms of row and coloumn):\n")


row = int(place[0])
coloumn = int(place[1])

new_row = row - 1
new_coloumn = coloumn - 1

map[new_coloumn][new_row] = "X" 
print(f"{row1}\n{row2}\n{row3}")
