input1 = str(input("Input : "))
panjang = len(input1)
print("Output :")

for i in range(panjang):
    for j in range(panjang-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(input1[j],end=" ")
    print()

for i in range(panjang):
    for j in range(i):
        print(" ",end=" ")
    for j in range(panjang-i):
        print(input1[j],end=" ")
    print()