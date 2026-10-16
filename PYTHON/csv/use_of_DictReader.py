import csv
fichier_source = "Extraction python des pages web/PYTHON/csv/fichier.csv"

with open(fichier_source, encoding="utf-8") as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])
        print(ligne)