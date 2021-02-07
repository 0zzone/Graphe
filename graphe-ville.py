# On importe les différentes bibliothèques et on lit le JSON
from time import sleep
import json
with open('villes.json') as json_file:
    data = json.load(json_file)


def tableau_villes(t):
    """ Cette fonction permet de transformer un tableau en chaîne de caractères. """
    if t == []:
        return 'aucune ville '
    liste = ''
    for i in t:
        liste = liste+''+str(i) + ', '
    return liste


# On définit les variables importantes du programme
villes = ['Parme', 'La Spezia', 'Bologne', 'Florence', 'Perouse', 'Rome']
choix = ['distance', 'temps', 'prix']
unite = ['km', 'min', '€']



def recherche(start, debut, fin, val, tab, numero):
    """ Cette fonction permet de renvoyer le chemin le plus optimisé pour aller d'un point A à B en fonction d'une contrainte. """
    if debut == fin:
        return "Il y erreur, car la ville de départ est la même que celle d'arrivée."
    if fin in data[debut]:
        return "Pour aller de " + str(start) + " à " + str(fin) + " , il faut passer par " + str(tableau_villes(tab)) + "pour un(e) " + choix[numero-1] + " de " + str(val+data[debut][fin][choix[numero-1]]) + " " + unite[numero-1] + "."
    else:
        t=[i for i in data[debut]]
        for i in range(len(t)-1):
            if t[i] in tab:
                return('Ville déjà visitée !')
            return min(recherche(start, t[i], fin, val+data[debut][t[i]][choix[numero-1]], tab+[t[i]], numero), recherche(start, t[i+1], fin, val+data[debut][t[i+1]][choix[numero-1]], tab+[t[i+1]], numero))




def itineraire():
    """ Cette fonction permet de rendre le code plus fluide à l'utilisation pour un utilisateur tiers. """
    print('------------------------------------------------------------------------------------------')
    print('Voilà la liste des destinations proposées par l\'agence:')
    sleep(0.5)
    print('\n 1) Parme \n 2) La Spezia \n 3) Bologne \n 4) Florence \n 5) Pérouse \n 6) Rome')

    print()
    print()

    sleep(1)

    print('Veuillez choisir la ville de départ et la ville d\'arrivée grâce au numéro de chaque ville:')

    r='N'
    while r=='N':
        depart = int(input('Ville de départ: '))
        destination = int(input('Ville d\'arrivée: '))
        while 1 > depart and depart==destination or depart > 6:
            print('Vous avez commis une erreur, rééssayez.')
            depart = int(input('Ville de départ: '))
        while 1 > destination or destination > 6 or depart==destination:
            print('Vous avez commis une erreur, rééssayez.')
            destination = int(input('Ville d\'arrivée: '))
        print('Départ : '+ villes[depart-1]+ ' --> destination : '+ villes[destination-1])
        r=(input('Veuillez confirmer votre trajet en rentrant Y. Si vous souhaitez le redéfinir, rentrez N: '))



    depart = villes[depart-1]
    destination = villes[destination-1]

    print()

    print('Vous avez la possibilité de choisir une contrainte de voyage: \n 1) L\'itinéraire le plus court \n 2) L\'itinéraire le plus rapide \n 3) L\'itinéraire le moins cher')
    choix = int(input('Votre choix: '))
    if choix < 1 or choix > 3:
        print('Vous venez de faire une erreur, réésayez.')

        choix = int(input('Votre choix: '))

    print(recherche(depart, depart, destination, 0, [], int(choix)))


itineraire()