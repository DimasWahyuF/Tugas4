class Jam :
    def init(self,jam,menit,detik):
        self.jm = jam
        self.mnt = menit
        self.dtk = detik 


def tampil():
    jam = int(input("Masukan Jam : "))
    menit = int(input("Masukan Menit : "))
    detik = int(input("Masukan Detik: "))

    if jam <=24 and menit <= 59 and detik <= 59:
        fJam = Jam(jam,menit,detik)
        print("Tugas Jam".center(30,"="))
        print("""
        Jam : {}
        Menit : {}
        Detik : {}
        """.format(fJam.jm,fJam.mnt,fJam.dtk))
        print("=".center(30,"="))
    else: 
        print("salah")
    
tampil()