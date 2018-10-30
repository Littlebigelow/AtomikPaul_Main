#Reading from a finalizePlayers
file_name = str(input("Name of text file"))

with open(file_name) as file:
    lines = file.readlines()
    print(''.join(lines))
