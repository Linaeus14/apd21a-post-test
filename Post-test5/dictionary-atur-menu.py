"""
Nama    : Tito Darmawan
NIM     : 02109106042
Prodi   : Informatika A
"""
#======================================================

ma = "makanan"
hama = "harga makanan"
mi = "minuman"
hami = "harga minuman"
menu = { 
 #makanan
 ma : [
 "Nasi Goreng",
 "Mi Goreng",
 "Ayam Goreng",
 "Martabak"
 ],
 #harga makanan
 hama : [
 15000, 
 12000, 
 10000,
 10000
 ],
 #minuman
 mi : [
 "Kopi",
 "Susu",
 "Teh",
 "Jus"
 ],
 #3 harga minuman
 hami : [
 5000,
 6000,
 4000,
 5000
 ]
}
menuinp = [
    [1, 2, 3, "stop"],
    [1, 2]
]

def salahinp(x, y):
    if not(x in menuinp[y]):
        print(
         ""
         "\nInput salah, coba lagi!"
        )
def rp(x):
    return "Rp."+str(x)+".00"

menu1 =""
while menu1 != "stop":
    menu1 = ""
    print("\nMENU")
    while not(menu1 in menuinp[0]):
        print(
         ""
         "\nMakanan"
        )
        z = -1
        for x in range(len(menu[ma])):
            z += 1
            print(
             f" {z+1}. {menu[ma][z]} : {rp(menu[hama][z])}"
            )
        print(
         ""
         "\nMinuman"
        )
        z = -1
        for x in range(len(menu[mi])):
            z += 1
            print(
             f" {z+1}. {menu[mi][z]} : {rp(menu[hami][z])}"
            )
        menu1 = input(
         ""
         f"""
Pengaturan Menu
(\"stop\" untuk keluar)
 > 1. Tambah Menu
   2. Hapus Menu
   3. Edit Menu
        
 > """
        )
        try:
            menu1 = int(menu1)
        except ValueError:
            menu1 = str(menu1)
        salahinp(menu1, 0)
    
    if menu1 == 1:
        menu2 = ""
        while not(menu2 in menuinp[1]):
            menu2 = input(
             ""
             """
 Pilih tipe menu untuk di tambah:
 > 1. Makanan
   2. Minuman

 > """
            )
            try:
              menu2 = int(menu2)
            except ValueError:
              menu2 = str(menu2)
            salahinp(menu2, 1)

            if menu2 == 1:
                addmenu = input(
                ""
                "\n Masukan nama makanan: "
                "\n >"
                )

                addmenu1 = ""
                while not(type(addmenu1) == int):
                    addmenu1 = input(
                    ""
                    "\n Masukan harga makanan: "
                    "\n >"
                    )
                    try:
                        addmenu1 = int(addmenu1)
                    except ValueError:
                        print(
                         "input bukan angka, coba lagi!"
                        )

                menu3 =""
                while not(menu3 in menuinp[1]):
                    menu3 = input(
                     ""
                     "\n  Tempat penambahan"
                     "\n> 1. Akhir menu"
                     "\n  2. Tengah menu"
                     "\n  Pilih Tempat penambahan : "
                     "\n> "
                    )
                    try:
                        menu3 = int(menu3)
                    except ValueError:
                        menu3 = str(menu3)
                    salahinp(menu3, 1)

                if menu3 == 1:
                    menu[ma].append(addmenu)
                    menu[hama].append(addmenu1)

                if menu3 == 2:
                    menu[ma].insert(round(len(menu[ma])/2), addmenu)
                    menu[hama].insert(round(len(menu[hama])/2), addmenu1)

            if menu2 == 2:
                addmenu = input(
                ""
                "\n Masukan nama minuman: "
                "\n >"
                )

                addmenu1 = ""
                while not(type(addmenu1) == int):
                    addmenu1 = input(
                    ""
                    "\n Masukan harga minuman: "
                    "\n >"
                    )
                    try:
                        addmenu1 = int(addmenu1)
                    except ValueError:
                        print(
                         "input bukan angka, coba lagi!"
                        )

                menu3 =""
                while not(menu3 in menuinp[1]):
                    menu3 = input(
                     ""
                     "\n  Tempat penambahan"
                     "\n> 1. Akhir menu"
                     "\n  2. Tengah menu"
                     "\n  Pilih Tempat penambahan : "
                     "\n> "
                    )
                    try:
                        menu3 = int(menu3)
                    except ValueError:
                        menu3 = str(menu3)
                    salahinp(menu3, 1)

                if menu3 == 1:
                    menu[mi].append(addmenu)
                    menu[hami].append(addmenu1)

                if menu3 == 2:
                    menu[mi].insert(round(len(menu[mi])/2), addmenu)
                    menu[hami].insert(round(len(menu[hami])/2), addmenu1)

    if menu1 == 2:
        menu2 = ""
        while not(menu2 in menuinp[1]):
            menu2 = input(
             ""
             """
 Pilih tipe menu untuk di hapus:
 > 1. Makanan
   2. Minuman

 > """
            )
            try:
              menu2 = int(menu2)
            except ValueError:
              menu2 = str(menu2)
            salahinp(menu2, 1)

        if menu2 == 1:
            hapmenu = ""
            while not(type(hapmenu) == int):
                hapmenu = input(
                ""
                "\n Pilih makanan yang ingin di hapus"
                "\n (masukan angka urut saja, misal \"1\")"
                "\n> "
                )
                try:
                    hapmenu = int(hapmenu)
                except ValueError:
                    print(
                        "input bukan angka, coba lagi!"
                    )
            #menggunakan del dan pop untuk menghapus list
            del menu[ma][hapmenu-1]
            menu[hama].pop(hapmenu-1)

        if menu2 == 2:
            hapmenu = ""
            while not(type(hapmenu) == int):
                hapmenu = input(
                ""
                "\n Pilih minuman yang ingin di hapus"
                "\n (masukan angka urut saja, misal \"1\")"
                "\n> "
                )
                try:
                    hapmenu = int(hapmenu)
                except ValueError:
                    print(
                        "input bukan angka, coba lagi!"
                    )
            #menggunakan del dan pop untuk menghapus list
            del menu[mi][hapmenu-1]
            menu[hami].pop(hapmenu-1)

    if menu1 == 3:
        menu2 = ""
        while not(menu2 in menuinp[1]):
            menu2 = input(
             ""
             """
 Pilih tipe menu untuk di edit:
 > 1. Makanan
   2. Minuman

 > """
            )
            try:
              menu2 = int(menu2)
            except ValueError:
              menu2 = str(menu2)
            salahinp(menu2, 1)
        
        if menu2 == 1:
            edmenu = ""
            while not(type(edmenu) == int):
                edmenu = input(
                ""
                "\n Pilih makanan yang ingin di edit"
                "\n (masukan angka urut saja, misal \"1\")"
                "\n> "
                )
                try:
                    edmenu = int(edmenu)
                except ValueError:
                    print(
                        "input bukan angka, coba lagi!"
                    )
            
            menu[ma][edmenu-1] = input(
             ""
             f"\n {menu[ma][edmenu-1]}"
             "\n Ubah nama makanan menjadi"
             "\n> "
            )

            menu[hama][edmenu-1] = input(
             ""
             f"\n {menu[hama][edmenu-1]}"
             "\n Ubah harga makanan menjadi"
             "\n> "
            )

        if menu2 == 2:
            edmenu = ""
            while not(type(edmenu) == int):
                edmenu = input(
                ""
                "\n Pilih minuman yang ingin di edit"
                "\n (masukan angka urut saja, misal \"1\")"
                "\n> "
                )
                try:
                    edmenu = int(edmenu)
                except ValueError:
                    print(
                        "input bukan angka, coba lagi!"
                    )
            
            menu[mi][edmenu-1] = input(
             ""
             f"\n {menu[mi][edmenu-1]}"
             "\n Ubah nama minuman menjadi"
             "\n> "
            )

            menu[hami][edmenu-1] = input(
             ""
             f"\n {menu[hami][edmenu-1]}"
             "\n Ubah harga minuman menjadi"
             "\n> "
            )