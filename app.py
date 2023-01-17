import glob
import os

# Struktur Data Yang Akan Disimpan
TEMPLATE = {
    "nama": " "*50,
    "nohp": " "*50,
    "mbps": " "*50,
    "tagihan": " "*50,
}

# Tampilan Menu Customer
def menu():
    os.system("clear")
    print("Selamat Datang Di Program".center(60))
    print("Pemabyaran/Daftar Wifi".center(59) + "\n")
    print("1. Daftar Paket Wifi Kami")
    print("2. Pesan Paket Wifi ")

# Read Paket
def read_produk():
    os.system("clear")
    daftar_paket = glob.glob('paket wifi/*.txt')    
    pjng_file = len(daftar_paket)

    print("="*56)
    print("Berikut Daftar Produk Wifi Kami".center(53))
    print("="*56)
    for data in range(pjng_file):
        daftar_paket[data] = daftar_paket[data].replace(".txt"," ")
        print(daftar_paket[data])
    print("="*56)

    pilih_paket()

# User Memilih Paket dan Kecepatan Wifinya
def pilih_paket():
    paket_yg_dipilih = input("Masukkan Nama Paket\t: ") + ".txt"
    os.system("clear")
    with open(paket_yg_dipilih,"r") as file:
        data = file.readlines()
        pjng = len(data)
        
        no = 1
        print("="*25)
        print("Berikut Harga Paket Kami")
        print("="*25)
        for content in data:
            content = content.split(",")
            kecepatan_wifi = content[0].replace('\n', '')
            harga_paket = content[1].replace('\n', '')
            print(f"Kecepatan {no}\t: {kecepatan_wifi}")
            print(f"Harga Paket {no}\t: Rp{harga_paket} ribu/bulan")
            print("="*25)
            no+=1
    
    pilihan = int(input("Masukkan Nomor Pilihan Anda\t:"))
    simpan_pesanan(pilihan, paket_yg_dipilih)

# Menyimpan Pesanan Kedalam Data.txt
def simpan_pesanan(pilihan, paket_yg_dipilih):
    os.system("clear")
    nama = input("Masukkan Nama Anda       : ")
    nomor = input("Masukkan Nomor Hp Anda   : ")

    with open(paket_yg_dipilih,"r+") as file:
        data = file.readlines()
        for index,data in enumerate(data):
            data = data.split(",")
            pilihan -= 1
            if index == pilihan:
                break

    kecepatan_wifi = data[0]
    tagihan = data[1].replace("\n","")
    
    # struktur data di copy dari template
    database = TEMPLATE.copy()
    
    database["nama"] = nama + TEMPLATE["nama"][len(nama):]
    database["nohp"] = nomor  + TEMPLATE["nohp"][len(nomor):]
    database["mbps"] = kecepatan_wifi  + TEMPLATE["mbps"][len(kecepatan_wifi):]
    database["tagihan"] = tagihan  + TEMPLATE["tagihan"][len(tagihan):]

    data_str = f"{database['nama']},{database['nohp']},{database['mbps']},{database['tagihan']}\n"

    with open("data.txt","a") as file:
        file.write(data_str)

    struk_belanja(nama, nomor, kecepatan_wifi, tagihan)

# Print Data Customer dan Paket Yang Di pesan
def struk_belanja(nama, nomor, kecepatan_wifi, tagihan):
    print("="*17)
    print("Berikut Data Anda")
    print("="*17)
    print(f"Nama  : {nama}")
    print(f"No.Hp : {nomor}")
    
    print("="*18)
    print("Paket Yang Dipesan")
    print("="*18)
    print(f"Kecepatan Wifi : {kecepatan_wifi}")
    print(f"Tagihan        : Rp{tagihan.replace(' ', '')} ribu/bulan")

menu()
while True:
    user_options = input("Masukkan Opsi\t: ")
    match user_options:
        case "1": read_produk()
        # case "2": 

