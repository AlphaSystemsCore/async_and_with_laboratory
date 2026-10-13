# Understand resource cleanup

with open("practical_laboratory/message.txt", "r") as file:
    print(file.read())

with statement manages the file start and file ending by closing the file automatically
