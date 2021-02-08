# On importe les différentes bibliothèques et on lit le JSON
from time import sleep
import json
import time
import sys
with open('villes.json') as json_file:
    data = json.load(json_file)
with open('visite.json') as json_file:
    visites = json.load(json_file)

def tableau_villes(t):
    """ Cette fonction permet de transformer un tableau en chaîne de caractères. """
    liste = ''
    for i in t:
        liste = liste+''+str(i) + ', '
    return liste

def visite_locale(t):
    liste = 'Sur votre chemin, vous pourrez visiter '
    for i in t:
        liste = liste + visites[i]['lieu'] + " à " + i + ", "
    return liste


# On définit les variables importantes du programme
villes = ['Parme', 'La Spezia', 'Bologne', 'Florence', 'Perouse', 'Rome']
choix = ['distance', 'temps', 'prix']
article = ['une', 'un', 'un']
choix_text = ['le plus court.', 'le plus rapide.', 'le moins cher.']
unite = ['km', 'min', '€']

def recherche(start, debut, fin, val, tab, numero):
    """ Cette fonction permet de renvoyer le chemin le plus optimisé pour aller d'un point A à B en fonction d'une contrainte. """
    if debut == fin:
        return "Il y erreur, car la ville de départ est la même que celle d'arrivée."
    if fin in data[debut]:
        if tab == []:
            print('\033[32m')
            return "Pour aller de " + str(start) + " à " + str(fin) + ", vous aurez " + article[numero-1] + " " + choix[numero-1] + " de " + str(val+data[debut][fin][choix[numero-1]]) + " " + unite[numero-1] + "."
        print('\033[32m')
        return "Pour aller de " + str(start) + " à " + str(fin) + " , il faut passer par " + str(tableau_villes(tab)) + "pour " + article[numero-1] + ' ' + choix[numero-1] + " de " + str(val+data[debut][fin][choix[numero-1]]) + " " + unite[numero-1] + ". " + str(visite_locale(tab))
    else:
        t=[i for i in data[debut]]
        for i in range(len(t)-1):
            if not t[i] in tab:
                return min(recherche(start, t[i], fin, val+data[debut][t[i]][choix[numero-1]], tab+[t[i]], numero), recherche(start, t[i+1], fin, val+data[debut][t[i+1]][choix[numero-1]], tab+[t[i+1]], numero))
            return 'Ville déjà visitée'
def itineraire():
    """ Cette fonction permet de rendre le code plus fluide à l'utilisation pour un utilisateur tiers. """
    print('------------------------------------------------------------------------------------------')
    print()
    print('Voilà la liste des destinations proposées par l\'agence:')
    sleep(0.5)
    print('\033[35m')
    print('\n 1) Parme \n 2) La Spezia \n 3) Bologne \n 4) Florence \n 5) Pérouse \n 6) Rome')

    print()
    print()

    sleep(1)
    print('\033[0m')
    print('Veuillez choisir la ville de départ et la ville d\'arrivée grâce au numéro de chaque ville:')

    r='N'
    c=0
    while r!='Y':
        if c > 0:
            print('\033[31m')
            print('Trajet refusé !')
            sleep(1)
        print('\033[0m')
        depart = int(input('Ville de départ: '))
        destination = int(input('Ville d\'arrivée: '))
        while 1 > depart and depart==destination or depart > 6:
            print('Vous avez commis une erreur, rééssayez.')
            depart = int(input('Ville de départ: '))
        while 1 > destination or destination > 6 or depart==destination:
            print('Vous avez commis une erreur, rééssayez.')
            destination = int(input('Ville d\'arrivée: '))
        print('\n \033[33m' + villes[depart-1] + ' --> ' + villes[destination-1])
        print('\033[0m')
        r=(input('Veuillez confirmer votre trajet en rentrant Y. Si vous souhaitez le redéfinir, rentrez N: '))
        c+=1
    print('\033[32m')
    print('Trajet validé !')

    depart = villes[depart-1]
    destination = villes[destination-1]

    sleep(1)

    print()

    print('\033[0m')
    print('Vous avez la possibilité de choisir une contrainte de voyage: ')
    print('\033[35m')
    print(' \n 1) L\'itinéraire le plus court \n 2) L\'itinéraire le plus rapide \n 3) L\'itinéraire le moins cher')
    print('\033[0m')
    choix = int(input('\nVotre choix: '))
    if choix < 1 or choix > 3:
        print('Vous venez de faire une erreur, réésayez.')
        choix = int(input('Votre choix: '))
    print('\n \033[33m Le trajet ' + choix_text[choix-1] + ".")
    

    print()
    print()
    print('\033[96m')
    print('Je cogite ...')
    print()
    toolbar_width = 25
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))
    for i in range(toolbar_width):
        time.sleep(0.1)
        sys.stdout.write("#")
        sys.stdout.flush()
    sys.stdout.write("]\n")

    print(recherche(depart, depart, destination, 0, [], int(choix)))
    print()
    print('\033[0m')
    print('------------------------------------------------------------------------------------------')


itineraire()