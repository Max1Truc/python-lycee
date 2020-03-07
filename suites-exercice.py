prix_1_paquet = 10
jours_1_année = 365.25
paquets_par_jour = 2
argent_sur_epargne = 0
interets = 0.05

print("""
Énoncé:
Un ancien fumeur souhaite mettre de côté l'argent qu'il économise en arrêtant de
fumer ses habituels {} paquets par jour. Chaque 31 décembre il mettra l'argent
économisé pendant l'année sur un livret d'épargnes avec des intérêts de {}%.
Ces intérêts sont versés chaque 1er janvier.

On considère les données suivantes:
  - Un paquet de cigarettes coûte {}€
  - Une année contient {} jours, en prenant en compte les années bissextiles
  - Le livret d'épargnes contient {}€ au départ
""".format(paquets_par_jour, interets * 100, prix_1_paquet, jours_1_année, argent_sur_epargne))

argent_economise_par_an = prix_1_paquet * paquets_par_jour * jours_1_année

# On récupère le nombre d'années à simuler
got_data = False
nombre_annees_a_simuler = 0
while not got_data:
    data_str = input("Nombre d'années à simuler : ")
    try:
        nombre_annees_a_simuler = int(float(data_str))
        got_data = True
    except:
        print("Merci d'entrer un entier valide.\n")
print("%d années seront simulées.\n" % nombre_annees_a_simuler)

for annee in range(nombre_annees_a_simuler + 1):
    print("\nAnnée n°%d:" % annee)

    if annee == 0:
        print("Notre maigre fortune s'élève à {}€".format(argent_sur_epargne))
    else:
        print("On ajoute les {}€ économisés durant l'année précédente".format(argent_economise_par_an))
        argent_sur_epargne += argent_economise_par_an

        interets_annuels = round(argent_sur_epargne * interets, 2)
        print("On ajoute les {}€ d'intérêts versés par la banque".format(interets_annuels))
        argent_sur_epargne += interets_annuels

        print("Le livret contient maintenant {}€".format(argent_sur_epargne))
