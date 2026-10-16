
import csv

fichier_source = "Extraction python des pages web/PYTHON/csv/fichier.csv"
fichier_destination = "Extraction python des pages web/PYTHON/csv/fichier_pipe.csv"

# 1. Lecture du fichier d'origine (avec des virgules)
# 2. Écriture dans le nouveau fichier (avec des '|')
with (
    open(fichier_source, mode="r", encoding="utf-8") as f_in,
    open(fichier_destination, mode="w", newline="", encoding="utf-8") as f_out,
):

    lecteur = csv.reader(f_in, delimiter=",")
    scripteur = csv.writer(f_out, delimiter="|")

    for ligne in lecteur:
        scripteur.writerow(ligne)