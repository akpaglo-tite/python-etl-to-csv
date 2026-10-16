from bs4 import BeautifulSoup
import csv
#Chemin relatif des fichiers
source_html = "Extraction python des pages web/HTML/annuaire.html"
destination_file = "Extraction python des pages web/PYTHON/csv/HTML & CSV/employes_nettoye.csv"

#Extraction du contenu du site web
with open(source_html, 'r',encoding='utf-8') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

#Listes des données à enregistrer dans notre fichier csv
line_tr = soup.select("tbody tr")
en_tete = soup.select("thead th")

#Ouverture et écriture dans le fichier csv 
with open(destination_file, mode='w',newline='',encoding='utf-8') as csv_file:
    writer_csv = csv.writer(csv_file)
    thead =[]
    for line in en_tete :
        thead.append(line.string)
    writer_csv.writerow(thead)
    for line in line_tr :
        name = line.find(class_="nom").string
        poste = line.find(class_="poste").string
        email = line.find(class_="email").string
    
        if email == "Non renseigné":
            email = "contact@entreprise.com"
        writer_csv.writerow([name,poste.upper(),email])
        

        
    
    
    