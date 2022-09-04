
try:
    with open("C:\\Users\\carlo\\Desktop\\viier.txt", "r",) as read:
        var = read.read()
        var = var.swapcase()
    with open("C:\\Users\\carlo\\Desktop\\viier.txt", "w",) as write:
        write.write(var)

except FileNotFoundError:
    print("That file was not found :(")
    