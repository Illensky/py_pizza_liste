#def tri_personalise(e):
#    return len(e)


def afficher(collection, n_premiers_elements=-1):
    #collection.sort(key=tri_personalise) Permet de trier une collection , key permet de passer une fonction en argument pour trier comme on veux, reverse=True permet d'inverser le tri
    c = collection
    if not n_premiers_elements == -1:
        c = collection[0:n_premiers_elements]
    if len(c) == 0:
        print("------ AUCUNE PIZZA ------")
        return
    print(f"------- LISTE DE PIZZA ({len(c)}) ------")
    for item in c:
        print(item)
    print()
    print("------ PREMIERE PIZZA ------")
    print(c[0])
    print()
    print("------ DERNIERE PIZZA ------")
    print(c[-1])


def ajouter_pizza_utilisateur(collection):
    p = input("Quelle pizza souhaitez vous ajouter ? ")
    '''  ===== detection pizza exite deja v1 =====
    if pizza_existe(p, collection):
        print("ERREUR : Cette pizza existe déjà")
        ajouter_pizza_utilisateur(collection)
    '''
    if p.lower() in collection:    #===== detection pizza exite deja v2 =====
        print("ERREUR : Cette pizza existe déjà")
        ajouter_pizza_utilisateur(collection)
    else:
        collection.append(p)

''' ===== detection pizza exite deja v1 =====
def pizza_existe(p, collection):
    for i in collection:
        if p == i:
            return True
    return False
'''

pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]
vide = ()

ajouter_pizza_utilisateur(pizzas)
afficher(pizzas)
