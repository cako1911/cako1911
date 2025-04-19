import random
sayi = random.randint(1, 100)
while True:
    tahmin = int(input("Tahmininizi girin: "))
    if tahmin == sayi:
        print("Tebrikler doğru cevap")
        break
    elif tahmin < sayi:
        print("Daha büyük bir sayı olduğunu söyleyebilirim")
    else:
        print("Daha küçük bir sayı olduğunu söyleyebilirim")   