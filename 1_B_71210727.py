nilai=0
total=0
output= ("Total = ")
bilangan = int(input("Masukkan banyak bilangan : "))

while nilai <int(bilangan):
    nilai = nilai+1
    n = nilai
    if nilai%3==0:
        n = nilai * - 1
    elif nilai%7==0:
        n = 0
    total = total + n 
    if n>1 or n==0:
        output +=" + " + str(n)
    else:
        output += " " + str(n)

print(output)
print("Hasil perhitungan diatas ialah", total)