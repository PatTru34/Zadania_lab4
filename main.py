# Zadanie 1

# lista=[]
# for a in range(31):
#      lista.append(a*2)
#
#
# plik=open("dane.txt","a+")
# plik.writelines(str(lista))
# plik.close()


# Zadanie 2

# plik=open("dane.txt","r")
# pliki=plik.readlines()
# print(pliki)
#
# plik.close()

# Zadanie 3

# with open("tekst.txt",'a') as plik:
#     plik.writelines(["Lorem Ipsum is simply dummy text of the printing and typesetting industry.\nLorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.\n "])
#
# with open("tekst.txt","r") as plik:
#     print(plik.read())

# Zadanie 4
# class NaZakupy():
#     nazwa_produktu = None
#     ilosc = None
#     jednostka_miary = None
#     cena_jed = None
#
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#
#     def wyswietl_produkt(self):
#         print("""
#         Nazwa produktu: {},
#         Ilość: {},
#         Jednostka miary: {},
#         Cena jednostki: {}
#          """.format(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed))
#
#     def ile_produktu(self):
#         return "{} {}".format(self.ilosc,self.jednostka_miary)
#     def ile_kosztuje(self):
#         return float(self.ilosc)*float(self.cena_jed)
#
#
# zakupy=NaZakupy(
#     nazwa_produktu="Szynka Podwawelska",
#     ilosc="5",
#     jednostka_miary="kg",
#     cena_jed="34"
# )
#
# zakupy.wyswietl_produkt()
# print(zakupy.ile_produktu())
# print(zakupy.ile_kosztuje())
#
# Zadanie 5

# Zadanie 6

# class Robaczek():
#     x=None
#     y=None
#     krok=None
#
#
#     def __init__(self,x,y,krok=1):
#         self.x=x
#         self.y=y
#         self.krok=krok
#
#     def idz_w_gore(self,ile_krokow):
#         self.y+=ile_krokow*self.krok
#
#     def idz_w_dol(self, ile_krokow):
#         self.y -= ile_krokow * self.krok
#
#     def idz_w_lewo(self, ile_krokow):
#         self.x -= ile_krokow * self.krok
#
#     def idz_w_prawo(self, ile_krokow):
#         self.x += ile_krokow * self.krok
#
#     def pokaz_gdzie_jestes(self):
#         print("Jestem w punkcie {},{}".format(self.x,self.y))
#
# robak=Robaczek(1,1)
#
# robak.idz_w_lewo(4)
# robak.idz_w_gore(10)
# robak.idz_w_dol(5)
# robak.idz_w_prawo(6)
# robak.pokaz_gdzie_jestes()