class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def kitap_listesi(self):
        self.file.seek(0)
        print("Kütüphanede Kayıtlı Kitap Listesi:")
        for line in self.file:
            print(line.strip())

    def kitap_ekle(self, kitap_bilgisi):
        self.file.write(kitap_bilgisi + "\n")
        print("Kitap Başarıyla Eklendi...")

    def kitap_sil(self, kitap_ismi):
        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()
        for line in lines:
            if kitap_ismi not in line:
                self.file.write(line)
        print("Kitap Başarıyla Silindi...")

def menu():
    lib = Library()
    while True:
        print('''
        --------MENÜ--------
        1)KİTAP LİSTESİ
        2)KİTAP EKLE
        3)KİTAP SİL
        q)ÇIKIŞ''')
        secim = input("Seçiminizi Giriniz: ")
        
        if secim == "1":
            lib.kitap_listesi()
        elif secim == "2":
            kitap_bilgisi = input("Kitap Bilgilerini Aralarında Virgül Kullanarak Giriniz (AD,YAZAR,TARİH,SAYFA): ")
            lib.kitap_ekle(kitap_bilgisi)
        elif secim == "3":
            kitap_ismi = input("Silmek İstediğiniz Kitabı Giriniz: ")
            lib.kitap_sil(kitap_ismi)
        elif secim == "q" or "Q":
            break
        else:
            print("Geçersiz Seçim Yaptınız...")

if __name__ == "__main__":
    menu()
