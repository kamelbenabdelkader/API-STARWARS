import pandas as pd
import requests


element = ''

def recup(element):
    url = 'https://swapi.dev/api/'
    reponse = requests.get(url+element)
    if reponse.status_code == 200:
        data = reponse.json()
        dataok = pd.DataFrame(data['results'])
    else:
        print("votre requete avec votre api n'a pas aboutit")
    return dataok
