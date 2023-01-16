
nim = input("Masukkan NIM  = ")
name = input("Masukkan Nama = ")

print("NIM  = " + nim)
print("Nama = " + name)

print("Pilihan")
print("1. Cappuccino")
print("2. Teh")
print("3. Exit")

choose = input("Masukkan Pilihan : ")
choose = int(choose)

match choose:
    case 1:
        print("Memilih Cappuccino")
        price = int(input("Masukkan Harga : "))
        ppn = 10 / 100 * price
        totalPrice = price + ppn
        print("PPN         : Rp " + str(ppn) + ",-")
        print("Total Harga : Rp " + str(totalPrice) + ",-")
    case 2:
        print("Memilih Teh")
        price = int(input("Masukkan Harga : "))
        ppn = 10 / 100 * price
        totalPrice = price + ppn
        print("PPN         : Rp " + str(ppn) + ",-")
        print("Total Harga : Rp " + str(totalPrice) + ",-")
    case 3:
        print("Terimakasih! ^_^")
        exit
