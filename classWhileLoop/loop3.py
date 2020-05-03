names=['John', 'Michael','Terry', 'Eric', 'Tom','John', 'Michael','Terry', 'Eric', 'Tom', 'Tom']
search_name=input("Who are you looking for ? ")
for name in names:
    if search_name == name:
        print("he is in the list")
        break
print("The game is over")

a = [2,5,1]
s = 0
for element in a:
    s += element
print(s)

