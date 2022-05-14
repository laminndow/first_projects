from random import randint
# Asetetaan muuttujat

vastaus = randint(0,100)
peli = False

# Printataan peliin alku

print("*" * 22)
print("Tervetuloa pellaamaan")
print("*" * 22)

#Kysytään haluaako pelaaja pelata ja asetetaan pelin muuttujat sen mukaan

kysymys = input("Haluatko pelata? (kyllä/ei): ")
if kysymys == "kyllä":
    peli = True
    print("Aloitetaan peli!")
    print("Arvaa oikei luku!")
else: 
    print("Näkemisiin! :3")

while peli == True:
    arvaus = int(input("Syötä arvauksesi: "))
    if arvaus < vastaus:
        print("Oikea vastaus on suurempi")
    elif arvaus > vastaus:
        print(" Oikea vastaus on pienempi!")
    else:
        print("Arvasit oikein!")
        peli = False