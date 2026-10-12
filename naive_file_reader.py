
file = open("file.txt", "r")
contents = file.readlines()

for line in contents:
    print(line)

file.close()