import random

def roll() :
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True :                     #fungsi while buat Run suatu blok kode selagi kondisi nya = true benar sesuai
    pemain = input("mau berapa orang yang main? (2-6) =" )
    if pemain.isdigit () :
        pemain = int(pemain)
        if 2 <= pemain <= 6 :
            break
        else: 
            print("harus 2-6 pemain")
    else:
        print("gabisa bang, input ga valid")


skor_maks = 50
skor_pemain = [0] * pemain

while max(skor_pemain) < skor_maks :
    for pemain_idx in range(pemain):
        print("\npemain nomor ", pemain_idx + 1, "Giliran kamu!")
        print("total skor mu :", skor_pemain[pemain_idx], "\n")
        skor_sekarang = 0

        while True :
            harus_roll = input("mau roll? (y/n) ").lower()
            if harus_roll.lower() != "y" :
                break

            dadu = roll()
            if dadu == 1:
                print("dapet satu bang, gantian")
                skor_sekarang = 0
                break
            else :
                skor_sekarang += dadu
                print("kamu dapet= ", dadu)
                print("skor mu sekarang = ", skor_sekarang)

        skor_pemain[pemain_idx] += skor_sekarang
        print("total skor mu = ", skor_pemain[pemain_idx])

skor_tertinggi = max(skor_pemain)
pemenang= skor_pemain.index(skor_tertinggi)
print("pemain nomor = ", pemenang + 1, "!",
      "adalah pemenang dengan skor berjumlah = ", skor_tertinggi)