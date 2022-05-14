print("*" * 55)
print("Tervetuloa pelaamaan Arkkiluola fantasiaroolipeliä!")
print("*" * 55)

nimi = input("Mikä on nimesi?: ")
ika = int(input("Minkä ikäinen olet?: "))
if ika >= 18:
    print(f"Tervetuloa pelaamaan {nimi}. Olet {ika} vuotias ja tarpeeksi vanha pelaamaan.")

    haluatkopelata = input("Haluatko pelata peliä?: (kyllä / ei) ").lower()
    if haluatkopelata == "kyllä":
        print("Aloitetaan peli!")
        vasen_vai_oikea = input("Käännytkö vasemmalle vai oikealle? (vasen / oikea)?")
        if vasen_vai_oikea == "vasen":
            ans = input("Hyvä valinta! Jatkat matkaasi ja eteesi tulee lampi. Haluatko uida sen läpi vai kiertää sen. (läpi / kierrä)?")

        else:
            print("Putosit kielekkeeltä ja kuolit")
    
    else:
        print("Game Over")

else:
    print("Et ole tarpeeksi vanha pelaamaan")
