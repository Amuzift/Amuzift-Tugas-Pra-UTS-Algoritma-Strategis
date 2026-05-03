# Nama  : Ahmad Muzakky I
# NIM   : 24533909
# Tugas : Implementasi Algoritma Brute Force - TSP

from itertools import permutations

def hitung_jarak(rute, jarak):
    total = 0
    for i in range(len(rute) - 1):
        total += jarak[rute[i]][rute[i+1]]
    total += jarak[rute[-1]][rute[0]] 
    return total

def brute_force_tsp(jarak, n):
    kota = list(range(1, n))

    rute_terbaik = None
    jarak_terbaik = float('inf')  

    for p in permutations(kota):
        rute = [0] + list(p)
        total = hitung_jarak(rute, jarak)

        if total < jarak_terbaik:
            jarak_terbaik = total
            rute_terbaik = rute

    return rute_terbaik, jarak_terbaik

print("================================")
print(" Nama : Ahmad Muzakky I")
print(" NIM  : 24533909")
print("================================")
print(" TSP - Algoritma Brute Force")
print("================================\n")

n = int(input("Jumlah kota: "))

nama = []
print()
for i in range(n):
    k = input(f"Nama kota ke-{i+1}: ")
    nama.append(k)

print(f"\nMasukkan matriks jarak {n}x{n}")
print("(pisahkan dengan spasi, isi 0 untuk kota yang sama)\n")

matriks = []
for i in range(n):
    while True:
        try:
            baris = list(map(int, input(f"Jarak dari {nama[i]}: ").split()))
            if len(baris) != n:
                print(f"Harus {n} angka, coba lagi.")
                continue
            matriks.append(baris)
            break
        except:
            print("Input salah, coba lagi.")

print("\nMatriks Jarak:")

lebar = max(max(len(nama_i) for nama_i in nama), 5) + 2

print(" " * lebar, end="")
for i in range(n):
    print(f"{nama[i]:>{lebar}}", end="")
print()

for i in range(n):
    print(f"{nama[i]:>{lebar}}", end="")
    for j in range(n):
        print(f"{matriks[i][j]:>{lebar}}", end="")
    print()

print("\nSedang mencari rute terpendek...\n")
rute, jarak_min = brute_force_tsp(matriks, n)

print("================================")
print(" HASIL")
print("================================")

rute_str = ""
for i in rute:
    rute_str += nama[i] + " -> "
rute_str += nama[rute[0]]

print(f" Rute Terbaik : {rute_str}")
print(f" Total Jarak  : {jarak_min}")
print("================================")