import json
with open('villes.json') as json_file:
    data = json.load(json_file)


def tableau_villes(t):
    if t == []:
        return 'aucune ville'
    liste = ''
    for i in t:
        liste = liste+''+str(i) + ', '
    return liste



choix = ['distance', 'temps', 'prix']
unite = ['km', 'min', '€']
def recherche(start, debut, fin, val, tab, numero):
    if debut == fin:
        return "Il y erreur, car la ville de départ est la même que celle d'arrivée."
    if fin in data[debut]:
        return "Pour aller de " + str(start) + " à " + str(fin) + " , il faut passer par " + str(tableau_villes(tab)) + " pour un(e) " + choix[numero-1] + " de " + str(val+data[debut][fin][choix[numero-1]]) + " " + unite[numero-1]
    else:
        t=[i for i in data[debut]]
        for i in range(len(t)-1):
            return min(recherche(start, t[i], fin, val+data[debut][t[i]][choix[numero-1]], tab+[t[i]], numero), recherche(start, t[i+1], fin, val+data[debut][t[i+1]][choix[numero-1]], tab+[t[i+1]], numero))



villes = ['Parme', 'La Spezia', 'Bologne', 'Florence', 'Perouse', 'Rome']
def itineraire():
    print('Voilà la liste des destinations proposées par l\'agence: \n 1) Parme \n 2) La Spezia \n 3) Bologne \n 4) Florence \n 5) Pérouse \n 6) Rome')

    print()
    print()

    print('Veuillez choisir la ville de départ et la ville d\'arrivée grâce au numéro de chaque ville:')

    depart = int(input('Ville de départ: '))
    destination = int(input('Ville d\'arrivée: '))
    if depart < 0 or depart > 6 or destination < 0 or destination > 6:
        print('Vous avez commis une erreur, rééssayez.')

        depart = int(input('Ville de départ: '))
        destination = int(input('Ville d\'arrivée: '))
    depart = villes[depart-1]
    destination = villes[destination-1]

    print()

    print('Vous avez la possibilité de choisir une contrainte de voyage: \n 1) L\'itinéraire le plus court \n 2) L\'itinéraire le plus rapide \n 3) L\'itinéraire le moins cher')
    choix = int(input('Votre choix: '))
    if choix < 0 or choix > 3:
        print('Vous venez de faire une erreur, réésayez.')

        choix = int(input('Votre choix: '))
    
    print(recherche(depart, depart, destination, 0, [], int(choix)))


itineraire()