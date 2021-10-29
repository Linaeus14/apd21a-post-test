"""
Nama    : Tito Darmawan
NIM     : 02109106042
Prodi   : Informatika A
"""
#================================================
print("""
|>          Konverter Suhu Ke Celcius
|                  Di Terminal Python
|   -----------------------------------------              
| Tipe konversi                                 
| _______________________________ 
| ( masukan angka saja misal : 1)
| 1. Fahrenheit -> Celcius
| 2. Kelvin ->  Celcius
| 3. Reamur -> celcius
| ( masukan \"Behenti\" untuk menghentikan semua )"""
)

ula = ""
nsuhu = 0
konsuhu = 0
menu1inp = ""

kamuS = {
    "ulang" : ula,
    "nilai suhu awal" : nsuhu,
    "nilai suhu akhir" : konsuhu,
    "menu utama" :menu1inp,
}#Dictionary

while ula != "Berhenti" and ula != "berhenti":
    kamuS["ulang"] = ""
    kamuS["nilai suhu awal"] = 0
    kamuS["nilai suhu akhir"] = 0
    menu1inp = str(input(
     "|_|_____________________________________________________________________" 
     "\n| [Pilihan (masukan \"L\" untuk menunujukan list konversi lagi): "   
    ))

    while menu1inp == "L" or menu1inp == "l":
        print(
         "|"
         "\n| Tipe konversi"                                 
         "\n| _______________________________ "
         "\n| ( masukan angka saja misal : 1 )"
         "\n| 1. Fahrenheit -> Celcius"
         "\n| 2. Kelvin ->  Celcius"
         "\n| 3. Reamur -> celcius"
         "\n| ( masukan \"Behenti\" untuk menghentikan semua )"
         "|"
        )
        menu1inp = str(input(
         "|_|_____________________________________________________________________" 
         "\n| [Pilih salah satu (masukan \"L\" untuk menunujukan list konversi lagi): "   
        ))

    if menu1inp == "Berhenti" or menu1inp == "berhenti":
            ula = "Berhenti"

    while menu1inp != "L" and menu1inp != "1" and menu1inp != "2" and menu1inp != "3" and menu1inp != "Berhenti" and menu1inp != "berhenti":
      print(
         "| Bukan masukan valid, mohon coba lagi"
          )  
      menu1inp = str(input(
         "\n| [Pilihan (masukan \"L\" untuk menunujukan list konversi lagi): "
        ))
    
    if menu1inp == "1":
        nsuhu = float(input(
         """|_|_____________________________________________________________________
  | 
  |              Fahrenheit ke Celcius
  |          -----------------------------
  | Masukan suhu Fahrenheit yang ingin di konversi (Input angka) : """
         ))
        konsuhu = (nsuhu - 32) * 5 / 9
        print(
         f"""  | Hasil koversi {nsuhu} derajat F ke Celcius = {konsuhu} derajat C"""
        )

        while ula != "T" and ula != "t" and ula != "Berhenti" and ula != "berhenti": 
            ula = str(input(
             "  |"
             "\n  | Ingin menghitung lagi (Y/T) ? \n  | [Masukan \"Berhenti\" untuk menghentikan semua] \n _| [masukan \"T\" untuk kembali]: "
            ))
            while ula != "Y" and ula != "y" and ula != "T" and ula != "t" and ula != "Berhenti" and ula != "berhenti":
                print(
                 "  | Bukan masukan valid, mohon coba lagi"
                )  
                ula = str(input(
                 "  |"
                 "\n  | Ingin menghitung lagi (Y/T) ? \n  | [Masukan \"Berhenti\" untuk menghentikan semua] \n  | [masukan \"T\" untuk kembali]: "
                ))
            
            if ula == "Y" or ula == "y":
                while ula != "T" and ula != "t" and ula != "Berhenti" and ula != "berhenti":
                    nsuhu = float(input(
                    "  |\n  | Masukan suhu Fahrenheit yang ingin di konversi (Input angka) : "
                    ))
                    konsuhu = (nsuhu - 32) * 5 / 9
                    print(
                    f"""  | Hasil koversi {nsuhu} derajat F ke Celcius = {konsuhu} derajat C"""
                    )
                    ula = str(input(
                     "  |"
                     "\n  | Ingin menghitung lagi (Y/T) ? \n  | [Masukan \"Berhenti\" untuk menghentikan semua] \n  | [masukan \"T\" untuk kembali]: "
                    ))
        if ula == "Y" or ula == "y" or ula == "T" or ula == "t":
            ula = ""
    
    if menu1inp == "2":
        nsuhu = float(input(
         """|_|_____________________________________________________________________
  | 
  |               Kelvin ke Celcius
  |          -----------------------------
  | Masukan suhu Kelvin yang ingin di konversi (Input angka) : """
         ))
        konsuhu = nsuhu - 273.15
        print(
         f"""  | Hasil koversi {nsuhu} derajat K ke Celcius = {konsuhu} derajat C"""
        )

        while ula != "T" and ula != "t" and ula != "Berhenti" and ula != "berhenti": 
            ula = str(input(
             "  |"
             "\n  | Ingin menghitung lagi (Y/T) ? \n  | [Masukan \"Berhenti\" untuk menghentikan semua] \n _| [masukan \"T\" untuk kembali]: "
            ))
            while ula != "Y" and ula != "y" and ula != "T" and ula != "t" and ula != "Berhenti" and ula != "berhenti":
                print(
                 "  | Bukan masukan valid, mohon coba lagi"
                )  
                ula = str(input(
                 "  |"
                 "\n  | Ingin menghitung lagi (Y/T) ? \n  | [Masukan \"Berhenti\" untuk menghentikan semua] \n  | [masukan \"T\" untuk kembali]: "
                ))
            
            if ula == "Y" or ula == "y":
                while ula != "T" and ula != "t" and ula != "Berhenti" and ula != "berhenti":
                    nsuhu = float(input(
                    "  |\n  | Masukan suhu Kelvin yang ingin di konversi (Input angka) : "
                    ))
                    konsuhu = nsuhu - 273.15
                    print(
                    f"""  | Hasil koversi {nsuhu} derajat K ke Celcius = {konsuhu} derajat C"""
                    )
                    ula = str(input(
                     "  |"
                     "\n  | Ingin menghitung lagi (Y/T) ? \n  | [Masukan \"Berhenti\" untuk menghentikan semua] \n  | [masukan \"T\" untuk kembali]: "
                    ))
        if ula == "Y" or ula == "y" or ula == "T" or ula == "t":
            ula = ""
        
    if menu1inp == "3":
        nsuhu = float(input(
         """|_|_____________________________________________________________________
  | 
  |               Reamur ke Celcius
  |          -----------------------------
  | Masukan suhu Reamur yang ingin di konversi (Input angka) : """
         ))
        konsuhu = nsuhu / 0.8
        print(
         f"""  | Hasil koversi {nsuhu} derajat Re ke Celcius = {konsuhu} derajat C"""
        )

        while ula != "T" and ula != "t" and ula != "Berhenti" and ula != "berhenti": 
            ula = str(input(
             "  |"
             "\n  | Ingin menghitung lagi (Y/T) ? \n  | [Masukan \"Berhenti\" untuk menghentikan semua] \n _| [masukan \"T\" untuk kembali]: "
            ))
            while ula != "Y" and ula != "y" and ula != "T" and ula != "t" and ula != "Berhenti" and ula != "berhenti":
                print(
                 "  | Bukan masukan valid, mohon coba lagi"
                )  
                ula = str(input(
                 "  |"
                 "\n  | Ingin menghitung lagi (Y/T) ? \n  | [Masukan \"Berhenti\" untuk menghentikan semua] \n  | [masukan \"T\" untuk kembali]: "
                ))
            
            if ula == "Y" or ula == "y":
                while ula != "T" and ula != "t" and ula != "Berhenti" and ula != "berhenti":
                    nsuhu = float(input(
                    "  |\n  | Masukan suhu Reamur yang ingin di konversi (Input angka) : "
                    ))
                    konsuhu = nsuhu / 0.8
                    print(
                    f"""  | Hasil koversi {nsuhu} derajat Re ke Celcius = {konsuhu} derajat C"""
                    )
                    ula = str(input(
                     "  |"
                     "\n  | Ingin menghitung lagi (Y/T) ? \n  | [Masukan \"Berhenti\" untuk menghentikan semua] \n  | [masukan \"T\" untuk kembali]: "
                    ))
        if ula == "Y" or ula == "y" or ula == "T" or ula == "t":
            ula = ""
