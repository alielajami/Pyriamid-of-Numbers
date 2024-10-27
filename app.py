x = int(input("Enter a number: "))

if x < 1:
    print("x should be greater than 0")
else:
    for i in range(x):
        for j in range(i+1):
            print(j+1, end=" ")
        print()