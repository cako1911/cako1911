import math

gecmis = []

while True:
    
    sayi = input("Lütfen bir sayi giriniz (veya 'cikis' / 'gecmis' yazin): ")
    if sayi == "cikis":
        print("Programdan çikiliyor...")
        break
    elif sayi == "gecmis":
        print("\nIslem Gecmisi:")
        for kayit in gecmis:
            print(kayit)
        print()
        continue
    try:
        sayi = int(sayi)
    except ValueError:
        print("Geçersiz sayi girdiniz. Lütfen tekrar deneyin.")
        continue
    sayi1 = input('Lütfen bir sayi giriniz (veya "cikis" / "gecmis" yazin):' )
    if sayi1 == "cikis":
        print("Programdan çikiliyor...")
        break
    elif sayi1 == "gecmis":
        print("\nIslem Gecmisi:")
        for kayit in gecmis:
            print(kayit)
        print()
        continue
    try:
        sayi1 = int(sayi1)
    except ValueError:
        print("Geçersiz sayi girdiniz. Lütfen tekrar deneyin.")
        continue
    islem = input('Lütfen bir işlem girin (+, -, *, /) veya "cikis" / "gecmis" yazin: ')
    if islem == "cikis":
        print("Programdan çikiliyor...")
        break
    elif islem == "gecmis":
        print("\nIslem Gecmisi:")
        for kayit in gecmis:
            print(kayit)
        print()
        continue

    if islem == "+":
        sonuc = sayi + sayi1
    elif islem == "-":
        sonuc = sayi - sayi1
    elif islem == "*":
        sonuc = sayi * sayi1
    elif islem == "/":
        if sayi1 == 0:
            print("Hata: Sifira bölme hatasi oluştu!")
        else:
            sonuc = sayi / sayi1
    else:
        print("hatali secim yaptiniz..")

    print("Sonuç:", sonuc)
    kayit = f"{sayi} {islem} {sayi1} = {sonuc}"
    gecmis.append(kayit)


    


