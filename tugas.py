#fungsi persegi(luas)
def luas_persegi (panjang,lebar):
    return panjang * lebar
print(luas_persegi(5,3))

#fungfsi persegi(keliling)
def keliling_persegi(panjang,lebar):
    return 2 * (panjang + lebar)
print(keliling_persegi(10,4))

#fungsi angka
def format_angka(angka):
    return f"{angka:,}"
print(format_angka(125000))

#cek stok

def cek_stok (stok, jumlah):
    if stok >= jumlah:
        return True
    else:
        return False
print(cek_stok(15,10))
print(cek_stok(3,7))