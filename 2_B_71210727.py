nama = str(input("Masukkan nama : "))

kursi_list = []
nama_list = []

while nama != "STOP":
    nomor = "Masukkan nomor kursi "+nama+" : "
    memanggil_nomor = input(nomor)
    if memanggil_nomor not in kursi_list:
        kursi_list.append(memanggil_nomor)
        nama_list.append(nama)
    else:
        print("Mohon maaf kursi tersebut telah diisi!")
    nama = input("Masukan nama : ")
for i in range (len(kursi_list)):
    print("Kursi nomor %s telah diisi oleh %s"%(kursi_list[i],nama_list[i]))