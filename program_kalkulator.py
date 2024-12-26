import kalkulator

def main():
    print("Operasi Matematika")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    operasi = input("Pilih operasi (1/2/3/4): ")

    bilangan_1 = float(input("Masukkan bilangan pertama: "))
    bilangan_2 = float(input("Masukkan bilangan kedua: "))

    if operasi == '1':
        hasil = kalkulator.tambah(bilangan_1, bilangan_2)
        print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
    elif operasi == '2':
        hasil = kalkulator.kurang(bilangan_1, bilangan_2)
        print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
    elif operasi == '3':
        hasil = kalkulator.kali(bilangan_1, bilangan_2)
        print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
    elif operasi == '4':
        hasil = kalkulator.bagi(bilangan_1, bilangan_2)
        print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')
    else:
        print("Operasi tidak valid.")

if __name__ == "_main_":
    main()