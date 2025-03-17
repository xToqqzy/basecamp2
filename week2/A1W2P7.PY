position = input()

colum = position[0]
row = int(position[1])

colum_num = (ord(colum.upper()) - ord('A') + 1)

antwoord = colum_num+row

print(antwoord)

if antwoord % 2 == 0:
    print('black')
else:
    print("white")
