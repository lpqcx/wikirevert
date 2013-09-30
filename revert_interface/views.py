# Python
import urlparse
import urllib
import json
import datetime
import csv

import requests
import bs4

import logging

# Django
from django.http import *
from django.conf import settings

logger = logging.getLogger(__name__)

def wiki_page(request, article_name):
    url = r'http://en.wikipedia.org/wiki/%s' % article_name
    r = requests.get(url)
    logger.info(r.status_code)
    logger.info(r.headers['content-type'])
    logger.info(r.encoding)
    
    #do stuff to page here
    page_text = r.text
    soup = bs4.BeautifulSoup(page_text)
    soup.find(id="firstHeading").append('Hello World')
    
    
    return HttpResponse(unicode(soup))

def wiki_edit_page(request, article_name):
    url = r'http://en.wikipedia.org/w/index.php?title=%s&action=edit' % article_name
    r = requests.get(url)
    logger.info(r.status_code)
    logger.info(r.headers['content-type'])
    logger.info(r.encoding)
    
    #do stuff to page here
    page_text = r.text
    soup = bs4.BeautifulSoup(page_text)
    soup.find(id="firstHeading").append('Hello World')
    
    return HttpResponse(unicode(soup))
    








#These methods forward along any other Wiki things that get caught up
#Note the forward of index.php?action=edit to the edit method
def wiki_index_php(request):
    action = request.GET.get("action", None)
    if action is not None and action == "edit":
        title = request.GET.get("title","")
        return wiki_edit_page(request, title)
    
    payload = dict(request.GET)
    url = r'http://en.wikipedia.org/w/index.php'
    r = requests.get(url, params=payload)
    logger.info(r.status_code)
    logger.info(r.headers['content-type'])
    logger.info(r.encoding)
    return HttpResponse(r.text)

def wiki_api_php(request):
    payload = dict(request.GET)
    url = r'http://en.wikipedia.org/w/api.php'
    r = requests.get(url, params=payload)
    logger.info(r.status_code)
    logger.info(r.headers['content-type'])
    logger.info(r.encoding)
    return HttpResponse(r.text)











