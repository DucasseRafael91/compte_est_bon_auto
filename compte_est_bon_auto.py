#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

valeurs_disponibles = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
                       6, 6, 7, 7, 8, 8, 9, 9, 10, 10,
                       25, 50, 75, 100]

nombre_cible = random.randint(101, 999)
nombres_choisis = random.sample(valeurs_disponibles, 6)

print("Nombre à atteindre :", nombre_cible)
print("Nombres disponibles :", nombres_choisis)

best_solution = {
    "distance": float("inf"),
    "valeur": None,
    "étapes": []
}

def resoudre(liste_nombres, liste_etapes):
    global best_solution

    if len(liste_nombres) == 1:
        valeur_actuelle = liste_nombres[0][0]
        if valeur_actuelle == nombre_cible:
            best_solution["distance"] = 0
            best_solution["valeur"] = valeur_actuelle
            best_solution["étapes"] = liste_etapes.copy()
            return True
        else:
            ecart = abs(nombre_cible - valeur_actuelle)
            if ecart < best_solution["distance"]:
                best_solution["distance"] = ecart
                best_solution["valeur"] = valeur_actuelle
                best_solution["étapes"] = liste_etapes.copy()
        return False

    for i in range(len(liste_nombres)):
        for j in range(len(liste_nombres)):
            if i == j:
                continue

            value_a, expr_a = liste_nombres[i]
            value_b, expr_b = liste_nombres[j]

            reste = [liste_nombres[k] for k in range(len(liste_nombres)) if k != i and k != j]

            possible_results = [
                (value_a + value_b, f"{value_a} + {value_b} = {value_a + value_b}"),
                (value_a - value_b, f"{value_a} - {value_b} = {value_a - value_b}"),
                (value_b - value_a, f"{value_b} - {value_a} = {value_b - value_a}"),
                (value_a * value_b, f"{value_a} * {value_b} = {value_a * value_b}")
            ]

            if value_b != 0 and value_a % value_b == 0:
                possible_results.append((value_a // value_b, f"{value_a} / {value_b} = {value_a // value_b}"))
            if value_a != 0 and value_b % value_a == 0:
                possible_results.append((value_b // value_a, f"{value_b} / {value_a} = {value_b // value_a}"))

            for new_value, new_step in possible_results:
                if new_value < 0:
                    continue
                new_steps = liste_etapes + [new_step]
                if resoudre(reste + [(new_value, str(new_value))], new_steps):
                    return True

    return False

def main():
    initial_number = [(n, str(n)) for n in nombres_choisis]
    resoudre(initial_number, [])

    for step in best_solution["étapes"]:
        print(step)

    if best_solution["distance"] == 0:
        print("Le compte est bon !")
    else:
        print("Le compte n'est pas bon...")
        print(f"Meilleure approximation trouvée : {best_solution['valeur']} (écart de {best_solution['distance']})")

if __name__ == "__main__":
    main()