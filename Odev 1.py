class Kisi:
    def __init__(self, ad, yas, meslek):
        self.ad = ad
        self.yas = yas
        self.meslek = meslek

    def __str__(self):
        return f"İsim: {self.ad}\nYaş: {self.yas}\nMeslek: {self.meslek}"


class KisiArsivi:
    def __init__(self):
        self.kisiler = []

    def kisi_ekle(self, kisi):
        self.kisiler.append(kisi)

    def dosyaya_yazdir(self, dosya_adı):
        with open(dosya_adı, "w") as dosya:
            for kisi in self.kisiler:
                dosya.write(f"{kisi.ad},{kisi.yas},{kisi.meslek}\n")

    def dosyadan_ara(self, kisi_adi):
        with open("kisi_arsivi.txt", "r") as dosya:
            for satir in dosya:
                ad, yas, meslek = satir.strip().split(",")
                if ad == kisi_adi:
                    return Kisi(ad, yas, meslek)
        return None


arsiv = KisiArsivi()

while True:
    print("1- Kişi ekle")
    print("2- Kişi ara")
    print("3- Çıkış yap")

    secim = input("Seçiminizi yapın (1-3): ")

    if secim == "1":
        ad = input("İsim: ")
        yas = input("Yaş: ")
        meslek = input("Meslek: ")
        kisi = Kisi(ad, yas, meslek)
        arsiv.kisi_ekle(kisi)
        arsiv.dosyaya_yazdir("kisi_arsivi.txt")
        print("Kişi başarıyla eklendi.")
        print("-----------------------------------------")

    elif secim == "2":
        arama_adi = input("Aranacak kişinin adını girin: ")
        arama_sonucu = arsiv.dosyadan_ara(arama_adi)
        if arama_sonucu:
            print(arama_sonucu)
        else:
            print("Aradığınız kişi bulunamadı.")
        print("-----------------------------------------")

    elif secim == "3":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
        print("-----------------------------------------")