"""
Nama    : Tito Darmawan
NIM     : 02109106042
Prodi   : Informatika A
"""
#================================================
username = ""
password = ""
username_n = ""
password_n = ""
lisusername = ["admin"]
lispassword = ["0000"]
faillog = 0
loginsts = False

while faillog != 3:
    print(
    """
    =======================
            LOGIN
    =======================
    """)

    menu1inp = str(input(
    ""
    "\n > Buat akun baru? (y/t) : "
    ))

    while menu1inp != "y" and menu1inp != "t":
        print(
        " input salah, coba lagi!"
        )
        menu1inp = str(input(
        ""
        "\n > Buat akun baru? (y/t) : "
        
        ))

    if menu1inp == "y":
        print(
    """
    =======================
          BUAT AKUN
    =======================
    """)
        username_n = str(input(
        "   username : "
        ))
        password_n = str(input(
        "   password : "
        ))
        lisusername.append(username_n)
        lispassword.append(password_n)
        print(
         "\n > Akun telah di buat"
        )

    else:
        username = str(input(
        "   Username : "
        ))
        password = str(input(
        "   password : "
        ))

        if not(username in lisusername) or not(password in lispassword):
            print(
"""
=====================================
    DATA SALAH SILAHKAN COBA LAGI
=====================================
"""     )
            faillog += 1
            if faillog == 3:
                print(
"""
=====================================
            GAGAL LOGIN
      TERLALU BANYAK PERCOBAAN
=====================================
"""     )
        
        else:
            print(
             "\n      ++++++++++++++++++"
             "\n      + Berhasil masuk +"
             "\n      ++++++++++++++++++"
             "\n"
            )
            print(
            "\n       Selamat datang"
            "\n"
            )
            loginsts = True
    if loginsts:
        menu2inp = input(
         "\n   Pilihan (angka saja misal \"1\")"
         "\n   1. Berhenti"
         "\n   2. Kembali"
         "\n   Pilih : "
        )

        while menu2inp != "1" and menu2inp != "2":
            print(
             "Input salah, silahkan coba lagi!"
             "\n"
            )
            menu2inp = input(
             "\n   Pilihan (angka saja misal \"1\")"
             "\n   1. Berhenti"
             "\n   2. Kembali"
             "\n   Pilih : "
            )

        if menu2inp == "1":
            break