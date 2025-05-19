def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Bir sayıyı 0'a bölemezsiniz!"
    return x / y

def main():
    print("Basit Hesap Makinesi")
    print("İşlemler:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    secim = input("Bir işlem seçin (1/2/3/4): ")

    if secim not in ['1', '2', '3', '4']:
        print("Geçersiz seçim.")
        return

    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    if secim == '1':
        print("Sonuç:", toplama(sayi1, sayi2))
    elif secim == '2':
        print("Sonuç:", cikarma(sayi1, sayi2))
    elif secim == '3':
        print("Sonuç:", carpma(sayi1, sayi2))
    elif secim == '4':
        print("Sonuç:", bolme(sayi1, sayi2))

if __name__ == "__main__":
    main()
