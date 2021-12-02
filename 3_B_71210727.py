input_1 = input("Input : ")
tambahan = len(input_1)
print("Output : ")
for i in range(tambahan):
    print(input_1[:i])
for j in range(tambahan,0,-1):
    print(input_1[:j])