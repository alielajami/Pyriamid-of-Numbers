x = int(input("Enter a number: "))

if x < 1: # Error handeling
    print("x should be greater than 0")
else: # Start the pyramid app
    for i in range(x): # For rows
        for j in range(i+1): # For actual numbers on each row
            print(j+1, end=" ")
        print()
