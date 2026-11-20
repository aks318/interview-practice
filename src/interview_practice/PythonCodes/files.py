import os

print(os.getcwd())

with open("text1.txt", "r") as f:
    content = f.read()

    print(content)

with open("text1.txt", "w") as f:
    f.write("Its override")

with open("text1.txt", "a") as f:
    f.write("\nIts new line")