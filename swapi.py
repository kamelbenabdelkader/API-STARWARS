import pandas as pd
import requests


# ==========================================================================================>
# On crée une fonction qui va appeler l'api.
def recovery_url(categorie:str):
    https = "https://swapi.dev/api/"
    url = https + categorie
    if requests.get(url):
        reponse = requests.get(url)
        print("===> la requête s’est déroulée correctement")
    else:
        print("ERREUR : la requête s’est pas déroulée correctement")
    return reponse
# ==========================================================================================>
# On crée une fonction de convertion.
def convertion_json(reponse):
    try:
        contenu = reponse.json()
        print("===> La convertion en JSON à réussis.")
    except:
        print("ERREUR : la convertion à écouchée !")
    print()
    return contenu
# ==========================================================================================>
# On demande à l'utilisateur une catégorie
def demander_categorie():
    categorie = ""
    while True:
        choix = input(
            """Veuillez saisir une catégorie : 
            A) films
            B) planets
            C) people
            D) vehicles
            """)
        if choix == "A":
            categorie = "films"
            break
        elif choix == "B":
            categorie = "planets"
            break
        elif choix =="C":
            categorie = "people"
            break
        elif choix =="D":
            categorie = "vehicles"
            break
        else:
            print("ERREUR : veuillez saisir une valeur valide !")
        print()
    return categorie
# ==========================================================================================>
# On crée un dataframe.
def create_dataframe(contenu):
    df = pd.DataFrame(contenu['results'])
    return df
# ==========================================================================================>
# On crée la fonction qui va tous éxécuter.
def prepare_create_dataframe():
    print()
    categorie = demander_categorie()
    reponse = recovery_url(categorie)
    contenu = convertion_json(reponse)
    df = create_dataframe(contenu)
    print("Le DataFrame : ")
    return df
# ==========================================================================================>
##
