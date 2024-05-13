class Ogrenci:
    def __init__(self, ad, soyad, numara, ders, vize, final):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.ders = ders
        self.vize = vize
        self.final = final

    def hesapla_durum(self):
        pass  

class Onlisans(Ogrenci):
    def __init__(self, ad, soyad, numara, ders, vize, final, program):
        self.program = program
        super().__init__(ad, soyad, numara, ders, vize, final)

    def hesapla_durum(self):
        basari_notu = self.vize * 0.4 + self.final * 0.6
        return "Geçti" if basari_notu >= 50 else "Kaldı"

class Lisans(Ogrenci):
    def __init__(self, ad, soyad, numara, ders, vize, final, bolum):
        self.bolum = bolum
        super().__init__(ad, soyad, numara, ders, vize, final)

    def hesapla_durum(self):
        basari_notu = self.vize * 0.4 + self.final * 0.6
        return "Geçti" if basari_notu >= 50 else "Kaldı"

class YuksekLisans(Ogrenci):
    def __init__(self, ad, soyad, numara, ders, vize, final, anabilim_dal):
        self.anabilim_dal = anabilim_dal
        super().__init__(ad, soyad, numara, ders, vize, final)

    def hesapla_durum(self):
        basari_notu = self.vize * 0.3 - self.final * 0.7
        return "Geçti" if basari_notu >= 70 else "Kaldı"


def ogrenci_bilgilerini_listeye_kaydet(ogrenci_listesi, ogrenci):
    ogrenci_listesi.append(ogrenci)

def durum_goster(ogrenci):
    return f"{ogrenci.ad} {ogrenci.soyad} ({ogrenci.numara}): {ogrenci.hesapla_durum()}"

def listeleyen_fonksiyon(ogrenci_listesi):
    for ogrenci in ogrenci_listesi:
        print(f"{ogrenci.ad} {ogrenci.soyad} ({ogrenci.numara}) - Durum: {ogrenci.hesapla_durum()}")

# Örnek Kullanım
onlisans1 = Onlisans("Yunus", "Dolan", "123", "Matematik", 60, 70, "Bilgisayar Programcılığı")
lisans1 = Lisans("Esra", "Söğüt", "456", "Fizik", 40, 75, "Fizik Mühendisliği")
yüksek_lisans1 = YuksekLisans("Aslı", "Genç", "789", "Kimya", 35, 85, "Organik Kimya")

onlisans2 = Onlisans("Mahmut", "Dolan", "321", "Elektirik", 65, 75, "Bilgisayar Programcılığı")
lisans2 = Lisans("Meryem", "Demir", "654", "Fonksiyon", 45, 85, "Matematik Mühendisliği")
yüksek_lisans2 = YuksekLisans("Ahmet", "Gazi", "987", "Karbon", 45, 75, "Organik Kimya")


ogrenci_listesi = []
ogrenci_bilgilerini_listeye_kaydet(ogrenci_listesi, onlisans1)
ogrenci_bilgilerini_listeye_kaydet(ogrenci_listesi, lisans1)
ogrenci_bilgilerini_listeye_kaydet(ogrenci_listesi, yüksek_lisans1)

ogrenci_bilgilerini_listeye_kaydet(ogrenci_listesi, onlisans2)
ogrenci_bilgilerini_listeye_kaydet(ogrenci_listesi, lisans2)
ogrenci_bilgilerini_listeye_kaydet(ogrenci_listesi, yüksek_lisans2)

listeleyen_fonksiyon(ogrenci_listesi)
