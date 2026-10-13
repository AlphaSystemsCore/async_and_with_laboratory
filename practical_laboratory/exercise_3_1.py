file = open("practical_laboratory/message.txt")

try:
    print(file.read())

finally:
    file.close()