import requests as rq
from htmlentities import decode

base_url = "http://www.chucknorrisfacts.fr/api/get"
defaults = "?data=tri:alea;type:txt;nb:1"

def facts():
    fact = rq.get(base_url+defaults).json()[0]['fact'].replace('&#039;','\'')
    return decode(fact)
