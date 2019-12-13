from random import randint

nb_tirages = 1000

effectif_5 = 0

tirage_n = 0
while tirage_n < nb_tirages:
    for i in range(0, 100):
        if randint(1, 6) == 5:
            effectif_5 += 1
        tirage_n += 1

    print("Nombre de tirages :", tirage_n)
    print("Effectif des cinqs :", effectif_5)
    print("Fréquence des cinqs :", round(effectif_5 / tirage_n * 100, 2), "%")
    print("")
