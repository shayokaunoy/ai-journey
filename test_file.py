with open(r"E:\ai-journey\test.txt", "w") as f:
    f.write("pen" + "\n")
    f.write("book" + "\n")

with open(r"E:\ai-journey\test.txt", "r") as f:
    print(f.read())