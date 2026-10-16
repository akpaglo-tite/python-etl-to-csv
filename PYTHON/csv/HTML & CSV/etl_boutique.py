
import csv
from bs4 import BeautifulSoup

path_html = "Extraction python des pages web/HTML/boutique.html"
path_csv_file = "Extraction python des pages web/PYTHON/csv/HTML & CSV/produits_dispo.csv"

# 1. EXTRACT
with open(path_html, mode="r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

produits_html = soup.select(".produit")

# 2. TRANSFORM & LOAD
with open(path_csv_file, mode="w", newline="", encoding="utf-8") as file_csv:
    writer = csv.writer(file_csv, delimiter=",")

    # Écriture de l'en-tête
    writer.writerow(["nom", "prix"])

    # Traitement en UNE SEULE boucle
    for produit in produits_html:
        dispo = produit.find("p").string

        # Filtrage : On ne traite que les produits "En stock"
        if dispo == "En stock":
            nom = produit.find("h2").string
            prix_brut = produit.find("span").string

            # Nettoyage du prix
            prix_clean = float(prix_brut.replace("€", "").strip())

            # Écriture directe dans le fichier
            writer.writerow([nom, prix_clean])