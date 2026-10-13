file = open("practical_laboratory/message.txt")

try:
    print(file.read())

finally:
    file.close()

# finally is important, it guarantee cleanup code even when an error occurs
