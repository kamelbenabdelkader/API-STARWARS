import pandas as pd
import requests

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

# On crée une fonction de convertion.
def convertion_json(reponse):
    try:
        contenu = reponse.json()
        print("===> La convertion en JSON à réussis.")
    except:
        print("ERREUR : la convertion à écouchée !")
    print()
    return contenu

# On crée un dataframe.
def create_dataframe(contenu):
    df = pd.DataFrame(contenu['results'])
    return df
