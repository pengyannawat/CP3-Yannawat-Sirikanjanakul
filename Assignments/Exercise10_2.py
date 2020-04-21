start = int(input("Start: "))
step = int(input("Step: "))
result = str(0)
for i in range(5):
    result = result + str(start + step*i + 1)
    print(result)