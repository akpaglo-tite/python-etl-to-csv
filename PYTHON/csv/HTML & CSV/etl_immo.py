from bs4 import BeautifulSoup
import csv

path_html = "Extraction python des pages web/HTML/immobilier.html"
path_csv_file = "Extraction python des pages web/PYTHON/csv/HTML & CSV/appartements_actifs.csv"


with open(path_html, 'r', encoding='utf-8') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

# 1. On récupère la LISTE des articles
annonces_actifs = soup.find_all("article")

# 2. On parcourt CHAQUE article un par un
for annonce in annonces_actifs:
    # 'annonce' est désormais une seule balise HTML
    annonce_id = annonce["data-id"]
    annonce_statut = annonce["data-statut"]

    print(f"ID : {annonce_id} | Statut : {annonce_statut}")
