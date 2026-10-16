from bs4 import BeautifulSoup
with open("Extraction python des pages web/HTML/index.html",'r') as fichier:
    soup = BeautifulSoup(fichier,"html.parser")
#print(soup)
"""titre = soup.title
identifier = soup.find(id="titre")
print(titre.string,"\n",identifier.string)
"""
liste = soup.select('li')


produits = dict()
for i in range(len(liste)):
    valeur = liste[i].text.split("\n")
    cle = f"information_sur_produit_{i+1}"
    produits[cle] = valeur[1:-1]
for i,j in produits.items():
    print(f"{i}: {j}")
