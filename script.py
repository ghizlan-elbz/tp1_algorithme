import random

with open("fichier.txt", "r") as file:
    n = int(file.readline().strip())  
    matrice = []
    for _ in range(n):
        ligne = list(map(int, file.readline().split()))
        matrice.append(ligne)

noeud_depart = random.randint(0, n - 1)
visites = [noeud_depart]
arbre_mst = []
cout_total = 0

while len(visites) < n:
    min_valeur = float('inf')
    u = v = -1

    for i in visites:
        for j in range(n):
            if j not in visites and 0 < matrice[i][j] < min_valeur:
                min_valeur = matrice[i][j]
                u, v = i, j

    if v != -1:
        visites.append(v)
        arbre_mst.append((u + 1, v + 1, min_valeur))  
        cout_total += min_valeur

print("Arêtes de l'Arbre Couvrant Minimum :")
for u, v, poids in arbre_mst:
    print(f"{u} - {v} (poids: {poids})")

print("Coût total du MST :", cout_total)