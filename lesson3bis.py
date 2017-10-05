#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 07:21:55 2017

@author: cochet
"""

#import urllib2
import requests
import urllib.request
from bs4 import BeautifulSoup

urldell = 'https://www.cdiscount.com/search/10/pc+portable+hp.html?TechnicalForm.SiteMapNodeId=0&TechnicalForm.DepartmentId=10&TechnicalForm.ProductId=&hdnPageType=Search&TechnicalForm.ContentTypeId=16&TechnicalForm.SellerId=&TechnicalForm.PageType=SEARCH_AJAX&TechnicalForm.LazyLoading.ProductSheets=False&NavigationForm.CurrentSelectedNavigationPath=f%2F1%2F0k%2F0k%7C0k0c%7C0k0c01&FacetForm.SelectedFacets.Index=0&FacetForm.SelectedFacets.Index=1&FacetForm.SelectedFacets.Index=2&FacetForm.SelectedFacets.Index=3&FacetForm.SelectedFacets.Index=4&FacetForm.SelectedFacets.Index=5&FacetForm.SelectedFacets%5B5%5D=f%2F6%2Fdell&FacetForm.SelectedFacets.Index=6&FacetForm.SelectedFacets.Index=7&SortForm.SelectedSort=PERTINENCE&ProductListTechnicalForm.Keyword=pc%2Bportable%2Bhp&&_his_'
#urlacer = 'https://www.cdiscount.com/search/10/pc+portable+hp.html?TechnicalForm.SiteMapNodeId=0&TechnicalForm.DepartmentId=10&TechnicalForm.ProductId=&hdnPageType=Search&TechnicalForm.ContentTypeId=16&TechnicalForm.SellerId=&TechnicalForm.PageType=SEARCH_AJAX&TechnicalForm.LazyLoading.ProductSheets=False&NavigationForm.CurrentSelectedNavigationPath=f%2F1%2F0k%2F0k%7C0k0c%7C0k0c01&FacetForm.SelectedFacets.Index=0&FacetForm.SelectedFacets.Index=1&FacetForm.SelectedFacets.Index=2&FacetForm.SelectedFacets.Index=3&FacetForm.SelectedFacets.Index=4&FacetForm.SelectedFacets.Index=5&FacetForm.SelectedFacets.Index=6&FacetForm.SelectedFacets.Index=7&FacetForm.SelectedFacets.Index=8&FacetForm.SelectedFacets.Index=9&FacetForm.SelectedFacets.Index=10&FacetForm.SelectedFacets.Index=11&FacetForm.SelectedFacets.Index=12&FacetForm.SelectedFacets.Index=13&FacetForm.SelectedFacets.Index=14&FacetForm.SelectedFacets.Index=15&FacetForm.SelectedFacets.Index=16&FacetForm.SelectedFacets.Index=17&FacetForm.SelectedFacets.Index=18&SortForm.SelectedSort=PERTINENCE&ProductListTechnicalForm.Keyword=pc%2Bportable%2Bhp&&_his_'


def getSoupFromURL(url, method='get', data={}):

  if method == 'get':
    res = requests.get(url)
  elif method == 'post':
    res = requests.post(url, data=data)
  else:
    return None

  if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup
  else:
    return None



soup = getSoupFromURL(urldell)

class_result = "price"

#prix = soup.find_all('span', {"class": class_result})
prix = soup.find_all('span', {"class": class_result})

#print(price)     List des montants en gras rexcherchés sur balise 'td'

#print(data.text.strip())




