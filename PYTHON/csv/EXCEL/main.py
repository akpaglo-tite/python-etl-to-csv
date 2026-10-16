import csv

donnees = [
    ["Nom", "Âge", "Ville"],
    ["Alice", 30, "Paris"],
    ["Bob", 25, "Lyon"],
]

# Le point-virgule force Excel à découper chaque mot dans sa propre case
with open("Extraction python des pages web/PYTHON/csv/EXCEL/tableau.csv", mode="w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(donnees)