import json
with open('villes.json') as json_file:
    data = json.load(json_file)

def recherche(debut, fin, dis):
    if debut == fin:
        return dis
    if fin in data[debut]:
        return dis+data[debut][fin]['distance']
    else:
        t=[i for i in data[debut]]
        for i in range(len(t)-1):
            return min(recherche(t[i], fin, dis+data[debut][t[i]]['distance']), recherche(t[i+1], fin, dis+data[debut][t[i+1]]['distance']))

        

print(recherche('Rome', 'Parme', 0))