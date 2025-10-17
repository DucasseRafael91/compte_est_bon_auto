#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

grid_of_values = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
                  6, 6, 7, 7, 8, 8, 9, 9, 10, 10,
                  25, 50, 75, 100]

number_to_reach = random.randint(101, 999)
plates = random.sample(grid_of_values, 6)

print("Nombre à atteindre :", number_to_reach)
print("Nombres disponibles :", plates)

# Meilleure solution trouvée
best_result = {
    "distance": float("inf"),
    "value": None,
    "steps": []
}

def solve(numbers, steps):
    global best_result

    if len(numbers) == 1:
        current_val = numbers[0][0]
        if current_val == number_to_reach:
            best_result["distance"] = 0
            best_result["value"] = current_val
            best_result["steps"] = steps.copy()
            return True
        else:
            distance = abs(number_to_reach - current_val)
            if distance < best_result["distance"]:
                best_result["distance"] = distance
                best_result["value"] = current_val
                best_result["steps"] = steps.copy()
        return False

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue

            a_val, a_expr = numbers[i]
            b_val, b_expr = numbers[j]

            remaining = [numbers[k] for k in range(len(numbers)) if k != i and k != j]

            results = [(a_val + b_val, f"{a_val} + {b_val} = {a_val + b_val}"),
                       (a_val - b_val, f"{a_val} - {b_val} = {a_val - b_val}"),
                       (b_val - a_val, f"{b_val} - {a_val} = {b_val - a_val}"),
                       (a_val * b_val, f"{a_val} * {b_val} = {a_val * b_val}")]

            # Division
            if b_val != 0 and a_val % b_val == 0:
                results.append((a_val // b_val, f"{a_val} / {b_val} = {a_val // b_val}"))
            if a_val != 0 and b_val % a_val == 0:
                results.append((b_val // a_val, f"{b_val} / {a_val} = {b_val // a_val}"))

            for val, expr in results:
                if val < 0:
                    continue
                new_steps = steps + [expr]
                if solve(remaining + [(val, str(val))], new_steps):
                    return True  # Stop at exact match

    return False

def main():
    initial_numbers = [(n, str(n)) for n in plates]
    solve(initial_numbers, [])

    for step in best_result["steps"]:
        print(step)

    if best_result["distance"] == 0:
        print("Le compte est bon !")
    else:
        print("Le compte n'est pas bon...")
        print(f"Meilleure approximation trouvée : {best_result['value']} (écart de {best_result['distance']})")

if __name__ == "__main__":
    main()