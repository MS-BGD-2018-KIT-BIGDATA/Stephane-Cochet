#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:14:31 2017

@author: cochet with Christophe’s helps
"""
from bs4 import BeautifulSoup
import re
import requests
import grequests
import pandas as pd


def get_soup_for_url(url):
    res = requests.get(url)
    if res.status_code == 200:
        return BeautifulSoup(res.text, 'lxml')


# Se faire la main sur la region PACA: 2 pages d'annonces 
liste_urls = []
debut = 'https://www.leboncoin.fr/voitures/offres/provence_alpes_cote_d_azur/?o='
fin = '&q=zo%E9'
# 2 pages sur la region PACA
for i in range(1, 3):
    r = requests.get(debut+str(i)+fin).status_code
    if r == 200:
        liste_urls.append(debut+str(i)+fin)
    else:
        break

unsent_request = (grequests.get(url) for url in liste_urls)
results = grequests.map(unsent_request)
#  html_page = requests.get("https://www.leboncoin.fr/voitures/offres/provence_alpes_cote_d_azur/?o=1&q=zoe")
urls = []
for p in range(0, 1):
    soup = BeautifulSoup(results[p].content, 'html.parser')
    soup = soup.find('section', class_= "tabsContent block-white dontSwitch")
    for page in soup.find_all('a'):
        urls.append(page.get('href'))
#print(urls)


urls = ['http:' + urls[i] for i in range(1,len(urls))]

#  Voici la liste des 35 urls renvoyés dans la liste urls
#  ['http://www.leboncoin.fr/voitures/1188756843.htm?ca=21_s',
#  'http://www.leboncoin.fr/voitures/1315418874.htm?ca=21_s',
#  'http://www.leboncoin.fr/voitures/1311183506.htm?ca=21_s',
#  'http://www.leboncoin.fr/voitures/1315018745.htm?ca=21_s',
#  'http://www.leboncoin.fr/voitures/1304254184.htm?ca=21_s',

# Début analyse du contenu
soup = get_soup_for_url(urls[0])
soup = soup.find_all('section', class_ ="properties lineNegative")

# retour avec prix, modele en soup
print(soup)
 
