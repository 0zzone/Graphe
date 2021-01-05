

class Cellule:
	"""Une cellule d’une liste chaînée"""
	def __init__(self, v, s):
		self.valeur = v
		self.suivant = s

class File:
	"""structure de file"""
	def __init__(self):
		self.tete = None
		self.queue = None

	def est_vide(self):
		return self.tete is None

	def enfile(self, x):
		c = Cellule(x, None)
		if self.est_vide():
			self.tete = c
		else:
			self.queue.suivant = c
		self.queue = c

	def defile(self):
		if self.est_vide():
			raise IndexError("retirer sur une file vide")
		v = self.tete.valeur
		self.tete = self.tete.suivant
		if self.tete is None:
			self.queue = None
		return v




class Pile:
	"""structure de pile"""
	def __init__(self):
		self.sommet = None

	def est_vide(self):
		return self.sommet is None

	def empile(self, valeur):
		self.sommet = Cellule(valeur, self.sommet)


	def depile(self):
		assert not self.est_vide(), "La pile est vide"
		v = self.sommet.valeur
		self.sommet = self.sommet.suivant
		return v



class Graphe:
    def __init__(self):
        """Le constructeur permet d'initialiser un dictionnaire vide qui représentera le graphe"""
        self.graphe = {}

    def ajoute_sommet(self,s):
        """Cette fonction permet d'ajouter un sommet au graphe"""
        if not s in self.graphe:
            self.graphe[s] = []

    def ajoute_arete(self,s1,s2):
        """Cette fonction permet d'ajouter une arete entre deux sommets du graphe"""
        self.ajoute_sommet(s1)
        self.ajoute_sommet(s2)
        self.graphe[s1].append(s2)
        self.graphe[s2].append(s1)

    def arete(self,s1,s2):
        """Cette fonction permet de savoir si il existe une arete entre deux sommets du graphe"""
        if s1 in self.graphe[s2] and s2 in self.graphe[s1]:
            return True
        return False

    def sommets(self):
        """Cette fonction permet de renvoyer tous les sommets du graphe"""
        som = self.graphe.keys()
        return som

    def voisins(self,s):
        """Cette fonction permet de renvoyer l'ensemble des voisins d'un sommet du graphe"""
        vois = self.graphe[s]
        return vois

    def nombre_cle(self):
        """Cette fonction permet de renvoyer le nombre de sommets"""
        return len(self.graphe.keys())

    def nombre_arete(self):
        """Cette fonction permet de connaître le nombre d'arete(s) du graphe"""
        return len(self.graphe.values()) // 2

    def degre(self,s):
        """Cette fonction permet de renvoyer le degré d'un sommet du graphe"""
        return len(self.graphe[s])

    def max_degre(self):
        """Cette fonction permet de renvoyer le sommet qui est de plus grand degré du graphe"""
        l = 0
        for i in self.graphe:
            if len(self.graphe[i]) > l:
                l = len(self.graphe[i])
                som = i
        return som

    def bfs(self,s):
        a_visiter = File()
        a_visiter.enfile(s)
        sommets_visites = []
        while not a_visiter.est_vide():
            tmp = a_visiter.defile()
            if not tmp in sommets_visites:
                sommets_visites.append(tmp)
                tab = G.voisins(tmp)
                for i in tab:
                    if not i in sommets_visites:
                        a_visiter.enfile(i)
        return sommets_visites

    def chemin(self, debut, fin):
        pere = {}
        pere['s1'] = None
        a_visiter = File()
        a_visiter.enfile(debut)
        sommets_visites = []
        while not a_visiter.est_vide():
            tmp = a_visiter.defile()
            if not tmp in sommets_visites:
                sommets_visites.append(tmp)
                tab = G.voisins(tmp)
                for i in tab:
                    if not i in sommets_visites:
                        a_visiter.enfile(i)
                        pere[i] = tmp
        tabe = []
        if fin in pere:
            tabe.append(fin)
            debut = fin
            while pere[debut] != None:
                tabe.append(pere[debut])
                debut = pere[debut]

            new = []
            k = len(tabe) - 1
            while k >= 0:
                new.append(tabe[k])
                k -= 1
            return new
        else:
            return(fin + " n'est pas dans le graphe !")

    def profondeur(self, s):
        p = Pile()
        p.empile(s)
        sommets_visites = []
        while not p.est_vide():
            tmp = p.depile()
            if not tmp in sommets_visites:
                sommets_visites.append(tmp)
                vois = G.voisins(tmp)
                for i in vois:
                    if not i in sommets_visites:
                        p.empile(i)
        return sommets_visites

    def existe_chemin(self, s1, s2):
        tab = self.profondeur(s1)
        if s2 in tab:
            return True
        return False


    def cycle(self, s1):
        p = Pile()
        p.empile((s1, None))
        sommets_visites = []
        while not p.est_vide():
            (tmp, pere) = p.depile()
            if not tmp in sommets_visites:
                sommets_visites.append(tmp)
                vois = G.voisins(tmp)
                for i in vois:
                    if not i in sommets_visites:
                        p.empile((i, tmp))
                    elif pere != i:
                        return True
        return False





DICO = ["aime", "auge", "baie", "brie", "bris", "bure", "cage", "cale", "came", "cape",
        "cime", "cire", "cris", "cure", "dame", "dime", "dire", "ducs", "dues", "duos",
        "dure", "durs", "fart", "fors", "gage", "gaie", "gais", "gale", "gare", "gars",
        "gris", "haie", "hale", "hors", "hure", "iris", "juge", "jure", "kart", "laie",
        "lame", "lime", "lire", "loge", "luge", "mage", "maie", "male", "mare", "mari",
        "mars", "mere", "mers", "mime", "mire", "mors", "muet", "mure", "murs", "nage",
        "orge", "ours", "page", "paie", "pale", "pame", "pane", "pape", "pare", "pari",
        "part", "paru", "pere", "pers", "pipe", "pire", "pore", "prie", "pris", "pues",
        "purs", "rage", "raie", "rale", "rame", "rape", "rare", "rime", "rire", "sage",
        "saie", "sale", "sape", "sari", "scie", "sure", "taie", "tale", "tape", "tare",
        "tari", "tige", "toge", "tore", "tors", "tort", "trie", "tris", "troc", "truc"]


def construction(t):
    graphe = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    dic = t
    for mot in dic:
        tab = []
        for lettre in mot:
            for al in alpha:
                new = mot.replace(lettre,al)
                if new in dic and new != mot:
                    tab.append(new)
        graphe[mot] = tab
    return graphe

def echelle(debut, fin):
    boucle = 0
    g = construction(DICO)
    if fin in g:
        if fin in g[debut]:
            boucle += 1
            return boucle
        else:
            for k in g[debut]:
                if k in g:
                    if fin in g[k]:
                        boucle += 1
                        return boucle
                    else:
                        boucle += 1
                else:
                    boucle += 1
        return boucle
    else:
        return(fin + ' n\'est pas dans le dictionnaire')

    
print(construction(DICO))

print(echelle("pape", "paie"))


def ech(debut, fin):
    g = construction(DICO)
    boucle = 0
    if fin in g[debut]:
        boucle += 1
        return boucle
    else:
        for i in g[debut]:
            if i in g:
                if fin in g[i]:
                    boucle += 1
                    return boucle
                else:
                    boucle += 1
            else:
                boucle += 1
        return boucle


print(ech('pape','paie'))