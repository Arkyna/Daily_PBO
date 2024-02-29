class Buku:
    def __init__(self, judul, penulis, tahun_terbit, jumlah_halaman):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.jumlah_halaman = jumlah_halaman
        self.halaman_terbaca = 0
        self.catatan = []

    def baca(self, halaman):
        if halaman <= self.jumlah_halaman - self.halaman_terbaca:
            self.halaman_terbaca += halaman
            print(f"Anda telah membaca {halaman} halaman dari {self.judul}.")
        else:
            print("Anda telah mencapai akhir buku.")

    def tambah_catatan(self, halaman, catatan):
        self.catatan.append((halaman, catatan))
        print(f"Catatan ditambahkan pada halaman {halaman}.")
    
    def tampilkan_catatan(self):
        print(f"Catatan untuk {self.judul}: ")
        for halaman, catatan in self.catatan:
            print(f"Halaman {halaman}: {catatan}")

    def cek_status_bacaan(self):
        if self.halaman_terbaca == self.jumlah_halaman:
            print(f"Anda telah selesai membaca {self.judul}.")
        else:
            sisa_halaman = self.jumlah_halaman - self.halaman_terbaca
            print(f"Sisa {sisa_halaman} halaman lagi untuk dibaca.")

judul = input("Masukkan judul buku: ")
penulis = input("Masukkan nama penulis: ")
tahun_terbit = int(input("Masukkan tahun terbit: "))

jumlah_halaman = int(input("Masukkan jumlah halaman: "))

buku_saya = Buku(judul, penulis, tahun_terbit, jumlah_halaman)
halaman_dibaca = int(input("Berapa halaman yang ingin Anda baca? "))
buku_saya.baca(halaman_dibaca)

halaman_catatan = int(input("Halaman yang ingin ditambahkan Catatan: "))
catatan = input(f"Catatan yang ingin dimasukkan dalam halaman
{halaman_catatan}: ")
buku_saya.tambah_catatan(halaman_catatan, catatan)

buku_saya.tampilkan_catatan()
buku_saya.cek_status_bacaan()