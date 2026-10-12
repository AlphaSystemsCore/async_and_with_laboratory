# with manages the resource cycle, opening, and closing of a file even if an error occurs

with open("file.txt", "r") as file:
    content = file.read()

print(content)