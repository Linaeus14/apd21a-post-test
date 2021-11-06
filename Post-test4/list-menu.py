"""
Nama    : Tito Darmawan
NIM     : 02109106042
Prodi   : Informatika A
"""
#======================================================

menu = [
 #0 makanan
 ["Nasi Goreng",
 "Mi Goreng",
 "Ayam Goreng"
 ],
 #1 harga makanan
 [15000, 
 12000, 
 10000 
 ],
 #2 minuman
 ["Kopi",
 "Susu",
 "Teh"
 ],
 #3 harga minuman
 [5000,
 6000,
 4000
 ]
]

def rp(x):
    return "Rp."+str(x)+".00"

print("\nMENU")
print(
    ""
    "\nMakanan"
)
z = -1
for x in range(len(menu[0])):
    z += 1
    print(
        f" {z+1}. {menu[0][z]} : {rp(menu[1][z])}"
    )
print(
    ""
    "\nMinuman"
)
z = -1
for x in range(len(menu[2])):
    z += 1
    print(
        f" {z+1}. {menu[2][z]} : {rp(menu[3][z])}"
    )