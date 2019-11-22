from math import sqrt

while True:
    print("""
=== Calcul de fonctions dérivées pour certains cas particuliers ===

Attention :
 Le signe "^" représente les puissances dans le texte qui suit même si en Python il faut utiliser "**"
 L'expression "sqrt(x)" dans le texte qui suit représente la racine carrée de x

Merci de choisir la forme de la fonction étudiée et d'entrer son numéro :
1. f(x) = k tel que k appartient à l'ensemble des réels
2. f(x) = x tel que x appartient à l'ensemble des réels
3. f(x) = x² tel que x appartient à l'ensemble des réels
4. f(x) = x³ tel que x appartient à l'ensemble des réels
5. f(x) = x ^ n tel que x et n appartiennent à l'ensemble des réels
6. f(x) = 1 / x tel que x appartient à l'ensemble des réels non-nuls
7. f(x) = 1 / (x ^ n) tel que x et n sont des réels et x différent de 0 si n différent de -1 et de 0
8. f(x) = sqrt(x) tel que x est positif
9. f(x) = ax² + bx + c tel que x est un réel et a est différent de 0
Choisissez 99 pour quitter le programme.
""")

    choix = input("Choix : ")

    if choix == "1":
        print("La fonction est constante, f'(x) = 0")
        
    elif choix == "2":
        print("La fonction est linéaire et son coefficient directeur est 1, donc f'(x) = 1")
        
    elif choix in ("3", "4", "5", "6", "7", "8", "9"): # Fonctions nécessitant l'entrée de la valeur de x
        x_str = input("x = ")
        x = None
        
        try:
            x = int(x_str)
        except:
            print("Votre entrée de x est invalide !")
        
        if x != None:
            if choix in ("5", "7"): # Fonctions nécessitant l'entrée de n
                n_str = input("n = ")
                n = None
                
                try:
                    n = int(n_str)
                except:
                    print("Votre entrée de n est invalide !")
                
                if n != None:
                    if choix == "5":
                        print("f'(x) = n * x ^ (n-1)")
                        print("f'(", x, ") =", n * x**(n-1))
                    elif choix == "7":
                        if n != -1 and x == 0:
                            print("Vous n'avez pas respecté les valeurs de x demandées !")
                        else:
                            print("f'(x) = - n / ( x ^ (n+1) )")
                            print("f'(", x, ") =", -n / ( x ** (n + 1) ) )
            elif choix == "9":
                # Polinôme du second degré, on demande les valeurs de a, b et c
                a_str = input("a = ")
                a = None
                b_str = input("b = ")
                b = None
                c_str = input("c = ")
                c = None
                
                try:
                    a = int(a_str)
                except:
                    print("Votre entrée de a est invalide !")
                
                try:
                    b = int(b_str)
                except:
                    print("Votre entrée de b est invalide !")
                
                try:
                    c = int(c_str)
                except:
                    print("Votre entrée de c est invalide !")
                
                if a != None and b != None and c != None:
                    if a == 0:
                        print("La valeur littérale a doit être différente de 0 !")
                    else:
                        print("f'(x) = 2ax + b")
                        print("f'(", x, ") =", 2*a*x + b )
            elif choix == "3":
                print("f'(x) = 2x")
                print("f'(", x, ") =", 2 * x)
            elif choix == "4":
                print("f'(x) = 3x²")
                print("f'(", x, ") =", 3 * x **2)
            elif choix == "6":
                if x == 0:
                    print("La valeur littérale x doit être différent de 0 !")
                else:
                    print("f'(x) = - 1 / x²")
                    print("f'(", x, ") =", (-1 / (x**2)))
            elif choix == "8":
                if x < 0:
                    print("La valeur littérale x doit être positive !")
                else:
                    print("f'(x) = 1 / (2 * sqrt(6))")
                    print("f'(", x, ") =", 1 / (2 * sqrt(6)))
                
    elif choix == "99":
        break
    
    else:
        print("Choix invalide !")
    
    input("\nAppuyez sur entrée pour continuer...")
