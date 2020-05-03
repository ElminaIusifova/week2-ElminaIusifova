
names=['John', 'Michael','Terry', 'Eric', 'Tom','John', 'Michael','Terry', 'Eric', 'Tom' 'John', 'John','Tom', 'Eric', 'Tom']
for first_name_loop in names:
    name_count=0
    for second_name_loop in names:
        if first_name_loop==second_name_loop:
            name_count+1

