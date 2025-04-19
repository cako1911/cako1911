import math
gecmis = []
while True:
    
    sayi = input("Lütfen bir sayı giriniz (veya 'çıkış' yazın): ")
    if sayi == "çıkış":
        print("Programdan çıkılıyor...")
        break
    elif giris1 == "geçmiş":
        print("\n📜 İşlem Geçmişi:")
        for kayit in gecmis:
            print(kayit)
        print()  # boş satır
        continue
    try:
        sayi = int(sayi)
    except ValueError:
        print("Geçersiz sayı girdiniz. Lütfen tekrar deneyin.")
        continue
    sayi1 = input('Lütfen bir sayı giriniz (veya "çıkış" yazın): ')
    if sayi1 == "çıkış":
        print("Programdan çıkılıyor...")
        break
    try:
        sayi1 = int(sayi1)
    except ValueError:
        print("Geçersiz sayı girdiniz. Lütfen tekrar deneyin.")
        continue
    islem = input('Lütfen bir işlem girin (+, -, *, /) veya "çıkış": ')
    if islem == "çıkış":
        print("Programdan çıkılıyor...")
        break
    
    if islem == "+":
        sonuc = sayi + sayi1
    elif islem == "-":
        sonuc = sayi - sayi1
    elif islem == "*":
        sonuc = sayi * sayi1
    elif islem == "/":
        if sayi1 == 0:
            print("Hata: Sıfıra bölme hatası oluştu!")
        else:
            sonuc = sayi / sayi1
    else:
        print("hatali secim yaptiniz..")

    print("✅ Sonuç:", sonuc)
    kayit = f"{sayi1} {islem} {sayi2} = {sonuc}"
    gecmis.append(kayit)


    


