import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    pemain = input("Mau berapa orang yang main? (2-6) = ")
    if pemain.isdigit():
        pemain = int(pemain)
        if 2 <= pemain <= 6:
            break
        else:
            print("Harus 2-6 pemain!")
    else:
        print("Input tidak valid!")

skor_maks = 50
skor_pemain = [0] * pemain

while max(skor_pemain) < skor_maks:
    for pemain_idx in range(pemain):
        print("\nPemain nomor", pemain_idx + 1, "giliran Anda!")
        print("Total skor Anda:", skor_pemain[pemain_idx], "\n")
        skor_sekarang = 0

        while True:
            mau_roll = input("Mau roll? (y/n) ").lower()
            if mau_roll != 'y':
                break

            dadu = roll()
            if dadu == 1:
                print("Anda dapat 1! Giliran selesai.")
                skor_sekarang = 0
                break
            else:
                skor_sekarang += dadu
                print("Anda mendapatkan:", dadu)
                print("Skor sementara:", skor_sekarang)

        skor_pemain[pemain_idx] += skor_sekarang
        print("Total skor Anda sekarang:", skor_pemain[pemain_idx])

skor_tertinggi = max(skor_pemain)
pemenang = skor_pemain.index(skor_tertinggi)
print("\nPemain nomor", pemenang + 1, "menang dengan skor", skor_tertinggi, "!")