"""
Nama    : Tito Darmawan
NIM     : 02109106042
Prodi   : Informatika A

Note    : Program mengimport package \"datatime\" dan modul \"datatime\" untuk menggunakan penentu weekdays dan weekend
"""
#================================================

import datetime

tgl = datetime.datetime.now()

kamuS = {
 "Mon" : "Senin",
 "Tue" : "Selasa",
 "Wed" : "Rabu",
 "Thu" : "Kamis",
 "Fri" : "Jum'at",
 "Sat" : "Sabtu",
 "Sun" : "Minggu"
}
hargA = {
 "Nasi Goreng"  : 15000,
 "Mi Goreng"    : 12000,
 "Ayam Goreng"  : 10000,
 "Kopi"         : 5000,
 "Susu"         : 6000,
 "Teh"          : 4000
}
diskoN = {
 "Senin"    : (10 / 100),
 "Selasa"   : (10 / 100),
 "Rabu"     : (10 / 100),
 "Kamis"    : (10 / 100),
 "Jum'at"   : (10 / 100),
 "Sabtu"    : (5 / 100),
 "Minggu"   : (5 / 100),
 "A"        : (5 / 100),
 "B"        : (10 / 100),
 "C"        : (5 / 100)
}

lisweekday = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at"]
lisweekend = ["Sabtu", "Minggu"]

def rp(x):
    return "Rp."+str(x)+".00"

print(
 f"""
     Penghitung Diskon Menu Kafe
 ---------------------------------------
    Pilih Pesanan

    Makanan
    1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
    2. Mi Goreng - {rp(hargA["Mi Goreng"])}
    3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

    Minuman
    4. Kopi - {rp(hargA["Kopi"])}
    5. Susu - {rp(hargA["Susu"])}
    6. Teh - {rp(hargA["Teh"])}
 """
)

counterharga = 0
countera = 0
counterb = 0
count = 0
tmbh = ""
ula = ""
stop = ""

while stop != "akhiri":
    menu1inp = ""
    tmbh = ""
    if ula == "y":
        counterharga = 0
        countera = 0
        counterb = 0
        ula = ""
    menu1inp = str(input(
     ""
     "\n > Masukan pilihan"
     "\n   (angka saja misal \"1\", masukan \"stop\" untuk berhenti)  : "
    ))

    while menu1inp != "1" and menu1inp != "2" and menu1inp != "3" and menu1inp != "4" and menu1inp != "5" and menu1inp != "6" and menu1inp != "stop":
        print(
         ""
         "\n   Input salah, coba lagi!"
        )
        menu1inp = str(input(
         ""
         "\n > Masukan pilihan"
         "\n   (angka saja misal \"1\", masukan \"stop\" untuk berhenti)  : "
        ))

    if menu1inp == "stop":
        stop = "akhiri"

    if menu1inp == "1":
        count = int(input(
         ""
         "\n   -Nasi Goreng-"
         "\n > Berapa pesanan? (angka) : "
        ))
        countera += count
        counterharga += hargA["Nasi Goreng"] * count

        tmbh = "" 
        tmbh = str(input(
         ""
         "\n > Tambah pesanan lain? (y/t) : "
        ))

        while tmbh != "y" and tmbh != "t":
            print(
             ""
             "\n   Input salah, coba lagi!"
            )
            tmbh = str(input(
             ""
             "\n > Tambah pesanan lain? (y/t) : "
            ))

    if menu1inp == "2":
        count = int(input(
         ""
         "\n   -Mi Goreng-"
         "\n > Berapa pesanan? (angka) : "
        ))
        countera += count
        counterharga += hargA["Mi Goreng"] * count

        tmbh = "" 
        tmbh = str(input(
         ""
         "\n > Tambah pesanan lain? (y/t) : "
        ))

        while tmbh != "y" and tmbh != "t":
            print(
             ""
             "\n   Input salah, coba lagi!"
            )
            tmbh = str(input(
             ""
             "\n > Tambah pesanan lain? (y/t) : "
            ))

    if menu1inp == "3":
        count = int(input(
         ""
         "\n   -Ayam Goreng-"
         "\n > Berapa pesanan? (angka) : "
        ))
        countera += count
        counterharga += hargA["Ayam Goreng"] * count

        tmbh = "" 
        tmbh = str(input(
         ""
         "\n > Tambah pesanan lain? (y/t) : "
        ))

    if menu1inp == "4":
        count = int(input(
         ""
         "\n   -Kopi-"
         "\n > Berapa pesanan? (angka) : "
        ))
        counterb += count
        counterharga += hargA["Kopi"] * count

        tmbh = "" 
        tmbh = str(input(
         ""
         "\n > Tambah pesanan lain? (y/t) : "
        ))

        while tmbh != "y" and tmbh != "t":
            print(
             ""
             "\n   Input salah, coba lagi!"
            )
            tmbh = str(input(
             ""
             "\n > Tambah pesanan lain? (y/t) : "
            ))

    if menu1inp == "5":
        count = int(input(
         ""
         "\n   -Susu-"
         "\n > Berapa pesanan? (angka) : "
        ))
        counterb += count
        counterharga += hargA["Susu"] * count

        tmbh = "" 
        tmbh = str(input(
         ""
         "\n > Tambah pesanan lain? (y/t) : "
        ))   

        while tmbh != "y" and tmbh != "t":
            print(
             ""
             "\n   Input salah, coba lagi!"
            )
            tmbh = str(input(
             ""
             "\n > Tambah pesanan lain? (y/t) : "
            ))

    if menu1inp == "6":
        count = int(input(
         ""
         "\n   -Teh-"
         "\n > Berapa pesanan? (angka) : "
        ))
        counterb += count
        counterharga += hargA["Teh"] * count

        tmbh = "" 
        tmbh = str(input(
         ""
         "\n > Tambah pesanan lain? (y/t) : "
        ))

    if tmbh == "t":
        emon = ""
        emon = input(
         ""
         "\n > Pembayaran menggunakan E-Money? (y/t) : "
        )

        while emon != "y" and emon != "t":
            print(
             ""
             "\n   Input salah, coba lagi!"
            )
            emon = input(
             ""
             "\n > Pembayaran menggunakan E-Money? (y/t) : "
            )

        if emon == "y":
            if not(countera >= 2) and not(counterb >= 3) and kamuS[tgl.strftime("%a")] in lisweekday:
                counterhargadis = counterharga - ( counterharga * ( diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"]) )
                print(
                 ""
                 "\n > Diskon       : 1. Weekdays (10%)"
                 "\n                : 2. E-money (5%)"
                 "\n   Total Diskon : 15%"
                 "\n"
                 f"\n > Harga awal   : {rp(counterharga)}"
                 f"\n   Diskon       : " + rp(int( counterharga * ( diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )),
                 "\n"
                 f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                 "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                )

            if countera >= 2 and not(counterb >= 3) and kamuS[tgl.strftime("%a")] in lisweekday: 
                counterhargadis = counterharga - ( counterharga * ( diskoN["A"] +  diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )
                print(
                 ""
                 "\n > Diskon       : 1. Weekday (10%)"
                 "\n                  2. Pesan 2 Makanan (5%)"
                 "\n                  3. E-money (5%)"
                 "\n   Total Diskon : 20%"
                 "\n"
                 f"\n > Harga awal   : {rp(counterharga)}"
                 f"\n   Diskon       : " + rp(int( counterharga * ( diskoN["A"] +  diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )),
                 "\n"
                 f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                    )

            if not(countera >= 2) and counterb >= 3 and kamuS[tgl.strftime("%a")] in lisweekday:
                counterhargadis = counterharga - ( counterharga * ( diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )
                print(
                 ""
                 "\n > Diskon       : 1. Weekday (10%)"
                 "\n                  2. Pesan 3 Minuman (10%)"
                 "\n                : 2. E-money (5%)"
                 "\n   Total Diskon : 25%"
                 "\n"
                 f"\n > Harga awal   : {rp(counterharga)}"
                 f"\n   Diskon       : " + rp(int( counterharga * ( diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )),
                 "\n"
                 f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                        )

            if countera >= 2 and counterb >= 3 and kamuS[tgl.strftime("%a")] in lisweekday: 
                counterhargadis = counterharga - ( counterharga * ( diskoN["A"] + diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )
                print(
                 ""
                 "\n > Diskon       : 1. Weekday (10%)"
                 "\n                  2. Pesan 3 Minuman (10%)"
                 "\n                  3. Pesan 2 Minuman (5%)"
                 "\n                : 2. E-money (5%)"
                 "\n   Total Diskon : 30%"
                 "\n"
                 f"\n > Harga awal   : {rp(counterharga)}"
                 f"\n   Diskon       : " + rp(int( counterharga * ( diskoN["A"] + diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )),
                 "\n"
                 f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                        )


            if not(countera >= 2) and not(counterb >= 3) and kamuS[tgl.strftime("%a")] in lisweekend:
                counterhargadis = counterharga - ( counterharga * ( diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )
                print(
                 ""
                 "\n > Diskon       : 1. Weekend (5%)"
                 "\n                : 2. E-money (5%)"
                 "\n   Total Diskon : 10%"
                 "\n"
                 f"\n > Harga awal   : {rp(counterharga)}"
                 f"\n   Diskon       : " + rp(int( counterharga * ( diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )),
                 "\n"
                 f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                        )

            if countera >= 2 and not(counterb >= 3) and kamuS[tgl.strftime("%a")] in lisweekend:
                counterhargadis = counterharga - ( counterharga * ( diskoN["A"] +  diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )
                print(
                ""
                 "\n > Diskon       : 1. Weekend (5%)"
                 "\n                  2. Pesan 2 Makanan (5%)"
                 "\n                : 2. E-money (5%)"
                 "\n   Total Diskon : 15%"
                 "\n"
                 f"\n > Harga awal   : {rp(counterharga)}"
                 f"\n   Diskon       : " + rp(int( counterharga * ( diskoN["A"] +  diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )),
                 "\n"
                 f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                        )

            if not(countera >= 2) and counterb >= 3 and kamuS[tgl.strftime("%a")] in lisweekend:
                counterhargadis = counterharga - ( counterharga * ( diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )
                print(
                 ""
                 "\n > Diskon       : 1. Weekend (5%)"
                 "\n                  2. Pesan 3 Minuman (10%)"
                 "\n                : 3. E-money (5%)"
                 "\n   Total Diskon : 20%"
                 "\n"
                 f"\n > Harga awal   : {rp(counterharga)}"
                 f"\n   Diskon       : " + rp(int( counterharga * ( diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )),
                 "\n"
                 f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                        )

            if countera >= 2 and counterb >= 3 and kamuS[tgl.strftime("%a")] in lisweekend:
                counterhargadis = counterharga - ( counterharga * ( diskoN["A"] + diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )
                print(
                ""
                 "\n > Diskon       : 1. Weekend (5%)"
                 "\n                  2. Pesan 3 Minuman (10%)"
                 "\n                  3. Pesan 2 Minuman (5%)"
                 "\n                : 4. E-money (5%)"
                 "\n   Total Diskon : 25%"
                 "\n"
                 f"\n > Harga awal   : {rp(counterharga)}"
                 f"\n   Diskon       : " + rp(int( counterharga * ( diskoN["A"] + diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] + diskoN["C"] ) )),
                 "\n"
                 f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                        )

        if emon == "t":
            if not(countera >= 2) and not(counterb >= 3) and kamuS[tgl.strftime("%a")] in lisweekday:
                counterhargadis = counterharga - ( counterharga * diskoN[kamuS[tgl.strftime("%a")]] )
                print(
                ""
                "\n > Diskon       : 1. Weekdays (10%)"
                "\n   Total Diskon : 10%"
                "\n"
                f"\n > Harga awal   : {rp(counterharga)}"
                f"\n   Diskon       : " + rp(int( counterharga * diskoN[kamuS[tgl.strftime("%a")]] )),
                "\n"
                f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                )

            if countera >= 2 and not(counterb >= 3) and kamuS[tgl.strftime("%a")] in lisweekday: 
                counterhargadis = counterharga - ( counterharga * ( diskoN["A"] +  diskoN[kamuS[tgl.strftime("%a")]] ) )
                print(
                ""
                "\n > Diskon       : 1. Weekday (10%)"
                "\n                  2. Pesan 2 Makanan (5%)"
                "\n   Total Diskon : 15%"
                "\n"
                f"\n > Harga awal   : {rp(counterharga)}"
                f"\n   Diskon       : " + rp(int( counterharga * ( diskoN["A"] +  diskoN[kamuS[tgl.strftime("%a")]] ))),
                "\n"
                f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                    )

            if not(countera >= 2) and counterb >= 3 and kamuS[tgl.strftime("%a")] in lisweekday:
                counterhargadis = counterharga - ( counterharga * ( diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] ) )
                print(
                    ""
                    "\n > Diskon       : 1. Weekday (10%)"
                    "\n                  2. Pesan 3 Minuman (10%)"
                    "\n   Total Diskon : 20%"
                    "\n"
                    f"\n > Harga awal   : {rp(counterharga)}"
                    f"\n   Diskon       : " + rp(int( counterharga * ( diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] ))),
                    "\n"
                    f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                        )

            if countera >= 2 and counterb >= 3 and kamuS[tgl.strftime("%a")] in lisweekday: 
                counterhargadis = counterharga - ( counterharga * ( diskoN["A"] + diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] ) )
                print(
                    ""
                    "\n > Diskon       : 1. Weekday (10%)"
                    "\n                  2. Pesan 3 Minuman (10%)"
                    "\n                  3. Pesan 2 Minuman (5%)"
                    "\n   Total Diskon : 25%"
                    "\n"
                    f"\n > Harga awal   : {rp(counterharga)}"
                    f"\n   Diskon       : " + rp(int( counterharga * ( diskoN["A"] + diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] ))),
                    "\n"
                    f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                        )


            if not(countera >= 2) and not(counterb >= 3) and kamuS[tgl.strftime("%a")] in lisweekend:
                counterhargadis = counterharga - ( counterharga * diskoN[kamuS[tgl.strftime("%a")]] )
                print(
                    ""
                    "\n > Diskon       : 1. Weekend (5%)"
                    "\n   Total Diskon : 5%"
                    "\n"
                    f"\n > Harga awal   : {rp(counterharga)}"
                    f"\n   Diskon       : " + rp(int( counterharga * diskoN[kamuS[tgl.strftime("%a")]] )),
                    "\n"
                    f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                        )

            if countera >= 2 and not(counterb >= 3) and kamuS[tgl.strftime("%a")] in lisweekend:
                counterhargadis = counterharga - ( counterharga * ( diskoN["A"] +  diskoN[kamuS[tgl.strftime("%a")]] ) )
                print(
                    ""
                    "\n > Diskon       : 1. Weekend (5%)"
                    "\n                  2. Pesan 2 Makanan (5%)"
                    "\n   Total Diskon : 10%"
                    "\n"
                    f"\n > Harga awal   : {rp(counterharga)}"
                    f"\n   Diskon       : " + rp(int( counterharga * ( diskoN["A"] +  diskoN[kamuS[tgl.strftime("%a")]] ))),
                    "\n"
                    f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                        )

            if not(countera >= 2) and counterb >= 3 and kamuS[tgl.strftime("%a")] in lisweekend:
                counterhargadis = counterharga - ( counterharga * ( diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] ) )
                print(
                    ""
                    "\n > Diskon       : 1. Weekend (5%)"
                    "\n                  2. Pesan 3 Minuman (10%)"
                    "\n   Total Diskon : 15%"
                    "\n"
                    f"\n > Harga awal   : {rp(counterharga)}"
                    f"\n   Diskon       : " + rp(int( counterharga * ( diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] ))),
                    "\n"
                    f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                        )

            if countera >= 2 and counterb >= 3 and kamuS[tgl.strftime("%a")] in lisweekend:
                counterhargadis = counterharga - ( counterharga * ( diskoN["A"] + diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] ) )
                print(
                    ""
                    "\n > Diskon       : 1. Weekend (5%)"
                    "\n                  2. Pesan 3 Minuman (10%)"
                    "\n                  3. Pesan 2 Minuman (5%)"
                    "\n   Total Diskon : 20%"
                    "\n"
                    f"\n > Harga awal   : {rp(counterharga)}"
                    f"\n   Diskon       : " + rp(int( counterharga * ( diskoN["A"] + diskoN["B"] +  diskoN[kamuS[tgl.strftime("%a")]] ))),
                    "\n"
                    f"\n > Harga akhir  : {rp(int(counterhargadis))}"
                )
                ula = input(
                    "Kembali ke menu awal? (y, stop) : "
                )
                if ula == "stop":
                    stop = "akhiri"
                else:
                    print(
    f"""
        Penghitung Diskon Menu Kafe
    ---------------------------------------
        Pilih Pesanan

        Makanan
        1. Nasi Goreng - {rp(hargA["Nasi Goreng"])}
        2. Mi Goreng - {rp(hargA["Mi Goreng"])}
        3. Ayam Goreng - {rp(hargA["Ayam Goreng"])}

        Minuman
        4. Kopi - {rp(hargA["Kopi"])}
        5. Susu - {rp(hargA["Susu"])}
        6. Teh - {rp(hargA["Teh"])}
    """
                        )