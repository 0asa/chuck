import requests as rq
from htmlentities import decode

chuck_url = "http://api.icndb.com/jokes/random"

def facts():    
    payload = { 'escape': 'javascript' }
    fact = rq.get(chuck_url,params=payload).json()['value']['joke']
    return decode(fact)
