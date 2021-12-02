input_pertama = int(input("Input : "))
print("Output :")
for row in range(input_pertama):
    for col in range(input_pertama):
        if col==(input_pertama-1) or row==(input_pertama-1) or col+row+1==input_pertama:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
