# 1) Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28

fiyatlar = {
    "benzin": 39.35,
    "dizel": 41.71,
    "lpg": 20.28
}

# Kullanıcıdan bilgiler al
yakit_tipi = input("Yakıt tipi (benzin, dizel, lpg): ").lower()  
if yakit_tipi not in fiyatlar:
    print("Yanlış yakıt tipi! 'benzin', 'dizel' veya 'lpg' giriniz.")
    exit()

tuketim = float(input("Aracın 100 km'de tükettiği yakıt miktarı (litre): "))
mesafe = float(input("Gidilecek mesafe (km): "))

masraf = (tuketim / 100) * mesafe * fiyatlar[yakit_tipi]

print(f"{mesafe} km için {yakit_tipi} yakıt masrafı: {masraf:.2f} TL")


# 2) Bir öğrencinin 2 vize 1 final notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen harf notunu yazdırınız.
#    90-100 => AA
#    80-89  => BA
#    70-79  => BB
#    60-69  => CB
#    50-59  => CC
#    40-49  => DC

vize1 = float(input("1. Vize notunu giriniz: "))
vize2 = float(input("2. Vize notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

ortalama = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)


if 90 <= ortalama <= 100:
    harf = "AA"
elif 80 <= ortalama < 90:
    harf = "BA"
elif 70 <= ortalama < 80:
    harf = "BB"
elif 60 <= ortalama < 70:
    harf = "CB"
elif 50 <= ortalama < 60:
    harf = "CC"
elif 40 <= ortalama < 50:
    harf = "DC"