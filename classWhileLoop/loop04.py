names = ['Terry', 'John', 'John', 'Terry', 'John', 'Terry', 'Eric','Michael', 'Michael', 'George', 'Michael', 'Eric','Terry', 'Terry', 'Tural', 'Memmed']
names_set = set(names)
print(names_set)
for name_first_loop in names_set:
    name_count = 0
    for name_second_loop in names:
        if name_first_loop == name_second_loop:
            name_count += 1
    if name_count > 2:
        print(name_first_loop, 'istifadeci tehlukelidir, daxil oldugu say:', name_count )
print("For Loop done!")