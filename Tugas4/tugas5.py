class Product:

    # class attribute
    matkul = "PBO"
    
    #instance attribute
    def __init__(self, ID_produk, Nama_Produk, Harga, Jumlah):
        self.IDProduk = ID_produk
        self.Nama_Produk = Nama_Produk
        self.Harga = Harga
        self.Jumlah = Jumlah

# instantiate Mahasiswa class
a = Product("teh botol", 123456789)

# access the class attributes
print("A tergabung dalam {}".format(a.__class__.matkul))

# access the instance attributes
print("{} punya nim {}".format( a.IDProduk, a.Nama_Produk))