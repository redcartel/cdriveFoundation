name_in_list = []
name = input('to begin, press enter')

def enter_name(name):
    while True:
        if name != 'done':
            name = input('enter your names or type done to exit when done')
            name_in_list.append(name)
        else:
            print('you have exited the program')
            break

enter_name(name)
print(name_in_list)

name_in_list = name_in_list[:-1]
namelist = '\n'.join(name_in_list)


filename = input('save the namelist as')
with open(filename, "w") as f:
    f.write(namelist)