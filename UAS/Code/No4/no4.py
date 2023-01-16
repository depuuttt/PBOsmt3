def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("Error: Pembagian dengan nol.")
        return
    return hasil


hasil = bagi(5, 2)
print(hasil)
# Output: 2.5

hasil = bagi(5, 0)
print(hasil)
# Output: Error: Pembagian dengan nol.
