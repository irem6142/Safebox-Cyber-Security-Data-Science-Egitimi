class Film:
    def __init__(self, ad, vizyonTarih, konu):
        self.ad = ad
        self.vizyonTarih= vizyonTarih
        self.konu = konu

    def __str__(self):
        return f"Film ismi: {self.ad}\nVizyon Tarihi: {self.vizyonTarih}\nKonusus: {self.konu}"


class FilmArsivi:
    def __init__(self):
        self.filmler = []

    def film_ekle(self, film):
        self.filmler.append(film)

    def dosyaya_yazdir(self, dosya_adı):
        with open(dosya_adı, "w") as dosya:
            for film in self.filmler:
                dosya.write(f"{film.ad},{film.vizyonTarih},{film.konu}\n")

    def dosyadan_ara(self, film_adi):
        with open("film_arsivi.txt", "r") as dosya:
            for satir in dosya:
               ad,vizyonTarih,konu= satir.strip().split(",")
            if ad == film_adi:
                    return Film(ad, vizyonTarih,konu)
        return None


arsiv = FilmArsivi()

while True:
    print("1- Film ekle")
    print("2- Film ara")
    print("3- Çıkış yap")

    secim = input("Seçiminizi yapın (1-3): ")

    if secim == "1":
        ad = input("Film Adı: ")
        vizyonTarih = input("Film vizyon tarihi: ")
        konu= input("Filmin konusu: ")
        film = Film(ad, vizyonTarih,konu)
        arsiv.film_ekle(film)
        arsiv.dosyaya_yazdir("film_arsivi.txt")
        print("Film başarıyla eklendi.")
        print("-----------------------------------------")

    elif secim == "2":
        arama_adi = input("Aranacak filmin adını girin: ")
        arama_sonucu = arsiv.dosyadan_ara(arama_adi)
        if arama_sonucu:
            print(arama_sonucu)
        else:
            print("Aradığınız film bulunamadı.")
        print("-----------------------------------------")

    elif secim == "3":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
        print("-----------------------------------------")