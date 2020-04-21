PiramidLayer = int(input("Enter number of layers that you want :"))

for x in range(PiramidLayer):

    print(" " * (PiramidLayer - (x - 1)) + "*" * (x * 2 + 1))
