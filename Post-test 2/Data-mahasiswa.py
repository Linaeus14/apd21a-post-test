"""
Nama    : Tito Darmawan
NIM     : 02109106042
Prodi   : Informatika A
"""
#================================================
print(
 f"""
             Data Mahasiswa
( Memberhentikan akan menghilangkan data)
 ---------------------------------------"""
)

namlis = []
nimlis = []
umlis = []
tilis = []
belis = []
jklis = []

ula = ""

counter = 0

while ula != "Akhiri" and ula != "akhiri":
    print(
     "\nPilih opsi (angka saja misal 1) : "
     "\n 1. Isi Data Baru"
     "\n 2. Cek Data Keseluruhan"
     "\n 3. Cek Data Masukan Terakhir"
    )
    menu1inp = str(input(
     "\nPilihan (Masukan \"Akhiri\" untuk memberhentikan semuanya) : "
    ))

    while menu1inp != "1" and menu1inp != "2" and menu1inp != "3" and menu1inp != "Akhiri" and menu1inp != "akhiri":
        print(
         "Input salah, coba lagi!"
        )
        menu1inp = str(input(
         "\nPilihan (Masukan \"Akhiri\" untuk memberhentikan semuanya) : "
        ))
    
    if menu1inp == "Akhiri" or menu1inp == "akhiri":
        ula = "Akhiri"

    if menu1inp == "1":
        while ula != "T" and ula != "t" and ula != "Akhiri" and ula != "akhiri":
            counter += 1
            print(
        f"""
             Data Mahasiswa
----------------------------------------
                 No {counter}"""
            )
            nam = str(input(
            "Nama                : "
            ))
            namlis.append(nam)

            nim = int(input(
            "NIM (angka)         : "
            ))
            nimlis.append(nim)

            um = int(input(
            "Umur (angka)        : "
            ))
            umlis.append(um)

            ti = float(input(
            "Tinggi(cm)          : "
            ))
            while ti <= 0.0:
                print(
                "Input salah, coba lagi!"
                )
                ti = float(input(
                "Tinggi(cm)          : "
                ))
            tilis.append(ti)

            be = float(input(
            "Berat(kg)           : "
            ))
            while be <= 0.0:
                print(
                "Input salah, coba lagi!"
                )
                be = float(input(
                "Berat(kg)           : "
                ))
            belis.append(be)

            jk = str(input(
            "Jenis Kelamin(L/P)  : "
            ))
            while jk != "L" and jk != "l" and jk != "P" and jk != "p":
                print(
                "Input salah, coba lagi!"
                )
                jk = str(input(
                "Jenis Kelamin(L/K)  : "
                ))
            if jk == "l":
                jk = "L"
            if jk == "p":
                jk = "P"
            jklis.append(jk)

            kamuS_daftaR = {
                f"nama{counter}"            : nam,
                f"nim{counter}"             : str(nim),
                f"umur{counter}"            : str(um),
                f"tinggi{counter}"          : str(ti),
                f"berat{counter}"           : str(be),
                f"jeniskelamin{counter}"    : jk
            }
            
            ula = str(input(
             "\nData telah di rekam, ingin menambahkan data lain? (Y/T) : "
            ))
            while ula != "Y" and ula != "y" and ula != "T" and ula != "t" and ula != "akhiri" and ula != "Akhir":
                print(
                 "Input salah, coba lagi!"
                )
                ula = str(input(
                 "\nData telah di rekam, ingin menambahkan data lain? (Y/T) : "
                ))
        if ula != "Akhiri" and ula != "akhiri":
            ula = ""
    
    if menu1inp == "2":
        if namlis == []:
            print(
             "\nData kosong"
            )
        else:
            print(
                "---------------------------------------------------------"
                "\n         Daftar Data\n"
                "\nDari kiri ke kanan No 1 - "+str(counter),
                "\nDaftar Nama          : "+str(namlis),
                "\nDaftar NIM           : "+str(nimlis),
                "\nDaftar Umur          : "+str(umlis),
                "\nDaftar Tinggi        : "+str(tilis),
                "\nDaftar Berat         : "+str(belis),
                "\nDaftar Jenis Kelamin : "+str(jklis)
            )

    if menu1inp == "3":
        if namlis == []:
            print(
             "\n                Data Kosong"
            )
        else:
            print(
            "\nNo",counter,
            "\n\nNama            : "+kamuS_daftaR[f"nama{counter}"],
            "\nNIM             : "+kamuS_daftaR[f"nim{counter}"],
            "\nUmur            : "+kamuS_daftaR[f"umur{counter}"],
            "\nTinggi          : "+kamuS_daftaR[f"tinggi{counter}"],
            "\nBerat           : "+kamuS_daftaR[f"berat{counter}"],
            "\nJenis Kelamin   : "+kamuS_daftaR[f"jeniskelamin{counter}"]
            )