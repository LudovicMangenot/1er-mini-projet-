from collections import Counter
# ETAPE 1
def occurrences_mots(texte):
    # Tokenisation du texte en mots
    mots = texte.split()

    # Utilisation de Counter pour compter les occurrences de chaque mot
    occurrences = Counter(mots)

    # Tri par nombre d'occurrences, en ordre décroissant
    occurrences_triees = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)

    return occurrences_triees

# Testons la fonction
texte_test = "Ceci est un test. Testons le code pour voir s'il fonctionne correctement."
resultat_test = occurrences_mots(texte_test)
print(resultat_test)



# ETAPE 2
def enlever_mots_parasites(occurrences, mots_parasites):
    # Filtrage des mots parasites
    occurrences_filtrees = [(mot, occ) for mot, occ in occurrences if mot.lower() not in mots_parasites]

    return occurrences_filtrees

# Testons la fonction
mots_parasites_test = ['le', 'la', 'les']
resultat_filtre = enlever_mots_parasites(resultat_test, mots_parasites_test)
print(resultat_filtre)




# ETAPE 3 
import csv

def lire_mots_parasites_csv(chemin_fichier):
    mots_parasites = []

    with open(chemin_fichier, 'r') as fichier:
        lecteur_csv = csv.reader(fichier)
        mots_parasites = next(lecteur_csv)

    return mots_parasites

# Testons la fonction avec un fichier CSV exemple
chemin_csv_test = 'parasites.csv'
mots_parasites_csv = lire_mots_parasites_csv(chemin_csv_test)
print(mots_parasites_csv)

# ETAPE 4 


# Etape 1
texte_long = " Les pirates sont mauvais ? Les Marines sont justes !? Ces termes ont toujours changé au cours de l’histoire ! Les enfants qui n’ont jamais vu la Paix et les enfants qui n’ont jamais vu la Guerre ont des valeurs différentes ! Ceux qui se tiennent au sommet déterminent ce qui est mal et ce qui est bien ! Cet endroit est un terrain neutre! La justice triomphera, dites-vous ? Mais bien sûr ça ira !!! Celui qui gagne cette guerre… Devient Justice"  #  chaîne de caractères assez longue
resultat_occurrences = occurrences_mots(texte_long)

# Etape 3
chemin_csv_test = 'parasites.csv'
mots_parasites_csv = lire_mots_parasites_csv(chemin_csv_test)

# Etape 2
resultat_filtre = enlever_mots_parasites(resultat_occurrences, mots_parasites_csv)
print(resultat_filtre)


# ETAPE 5

from bs4 import BeautifulSoup

def enlever_balises_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    texte_sans_balises = soup.get_text(separator=' ')
    return texte_sans_balises

# Testons la fonction avec une chaîne HTML
html_test = "<p>Ceci est <b>un exemple</b> de texte HTML.</p>"
texte_sans_balises = enlever_balises_html(html_test)
print(texte_sans_balises)


# ETAPE 6 

from bs4 import BeautifulSoup

def extraire_attribut_balise(html, nom_balise, nom_attribut):
    valeurs_attribut = []

    soup = BeautifulSoup(html, 'html.parser')
    balises = soup.find_all(nom_balise)

    for balise in balises:
        valeur = balise.get(nom_attribut)
        if valeur:
            valeurs_attribut.append(valeur)

    return valeurs_attribut

# Testons la fonction pour récupérer les valeurs des attributs alt des balises img
html_test = """
<html>
    <body>
        <img src="image1.jpg" alt="Description 1">
        <img src="image2.jpg" alt="Description 2">
        <img src="image3.jpg" alt="Description 3">
    </body>
</html>
"""

valeurs_alt = extraire_attribut_balise(html_test, 'img', 'alt')
print(valeurs_alt)



# ETAPE 7


# Fonction pour extraire les valeurs des attributs 'alt' des balises 'img'
valeurs_alt = extraire_attribut_balise(html_test, 'img', 'alt')
print("Valeurs des attributs 'alt' des balises 'img':", valeurs_alt)

# Fonction pour extraire les href des balises 'a'
valeurs_href = extraire_attribut_balise(html_test, 'a', 'href')
print("Valeurs des attributs 'href' des balises 'a':", valeurs_href)



# ETAPE 8 

from urllib.parse import urlparse

def extraire_nom_domaine(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

# Testons la fonction avec une URL
url_test = "https://www.example.com/path/to/page"
nom_domaine = extraire_nom_domaine(url_test)
print("Nom de domaine:", nom_domaine)



# ETAPE 9

def filtrer_urls_par_domaine(nom_domaine, liste_urls):
    urls_du_domaine = []
    urls_hors_domaine = []

    for url in liste_urls:
        if extraire_nom_domaine(url) == nom_domaine:
            urls_du_domaine.append(url)
        else:
            urls_hors_domaine.append(url)

    return urls_du_domaine, urls_hors_domaine

# Testons la fonction avec une liste d'URLs
liste_urls_test = [
    "https://www.example.com/page1",
    "https://www.example.com/page2",
    "https://www.otherdomain.com/page3",
]

nom_domaine_test = "www.example.com"
urls_du_domaine, urls_hors_domaine = filtrer_urls_par_domaine(nom_domaine_test, liste_urls_test)

print("URLs du domaine:", urls_du_domaine)
print("URLs hors du domaine:", urls_hors_domaine)



# ETAPE 10

import requests

def recuperer_html_depuis_url(url):
    try:
        reponse = requests.get(url)
        reponse.raise_for_status()  # Lève une exception en cas d'erreur HTTP

        html = reponse.text
        return html
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de la page ({url}): {e}")
        return None

# Testons la fonction avec une URL réelle
url_test = "https://www.example.com"
html_page = recuperer_html_depuis_url(url_test)

if html_page:
    print("Texte HTML de la page:")
    print(html_page)




# ETAPE 11

# Fonction pour faire l'audit de la page
def audit_page(url):
    # Récupère le texte HTML de la page
    html_page = recuperer_html_depuis_url(url)

    if html_page:
        # Enlève les balises HTML du texte
        texte_sans_balises = enlever_balises_html(html_page)

        # Obtient les occurrences des mots
        occurrences_mots_page = occurrences_mots(texte_sans_balises)

        # Enlève les mots parasites
        mots_parasites_csv = lire_mots_parasites_csv('parasites.csv')
        occurrences_filtrees = enlever_mots_parasites(occurrences_mots_page, mots_parasites_csv)

        # Obtient les valeurs des attributs 'alt' des balises 'img'
        valeurs_alt = extraire_attribut_balise(html_page, 'img', 'alt')

        # Obtient les valeurs des attributs 'href' des balises 'a'
        valeurs_href = extraire_attribut_balise(html_page, 'a', 'href')

        # Affiche les résultats
        print("Mots clés avec les 3 premières valeurs d'occurrences:")
        print(occurrences_filtrees[:3])

        print("\nNombre de liens entrants (balises 'a'):", len(valeurs_href))
        print("Nombre de liens sortants (balises 'a'):", len(valeurs_href))

        print("\nPrésence de balises alt (balises 'img'):")
        print("Oui" if valeurs_alt else "Non")

# Testons la fonction avec une URL réelle
url_audite = "https://www.example.com"
audit_page(url_audite)




