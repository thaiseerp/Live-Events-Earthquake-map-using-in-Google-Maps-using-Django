"""
Author: Thaiseer Parammal
"""

import requests
from bs4 import BeautifulSoup

def getlatlong():
    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.atom"
    source_code = requests.get(url)
    content = source_code.text
    con = BeautifulSoup(content, "html.parser")
    latlog = {}
    j = 1
    latlog[0] = 'Latitude and Longitude'
    for row1 in con.find_all('entry'):
        x = row1.text

        at = BeautifulSoup(x, "html.parser")
        i = 0
        for lat in at.findAll('dd'):
            if i == 2:
                latlog[j] = lat.text
            i += 1
        j += 1
    return latlog


def gettime():
    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.atom"
    source_code = requests.get(url)
    content = source_code.text
    con = BeautifulSoup(content, "html.parser")
    times = {}
    j = 1
    times[0] = 'Time of event'
    for row1 in con.find_all('entry'):
        x = row1.text

        at = BeautifulSoup(x, "html.parser")
        i = 0
        for time in at.findAll('dd'):
            if i == 0:
                times[j] = time.text
            i += 1
        j += 1
    return times


def gettitle():
    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.atom"
    source_code = requests.get(url)
    content = source_code.text
    con = BeautifulSoup(content, "html.parser")
    titles = {}
    i = 0
    for title in con.find_all('title'):
        titles[i] = title.text.splitlines()[0]
        i += 1
    return titles


def getlink():
    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.atom"
    source_code = requests.get(url)
    content = source_code.text
    con = BeautifulSoup(content, "html.parser")
    links = {}
    links[0] = 'links of events'
    i = 1
    for link in con.find_all('link', {'type': 'text/html'}):
        links[i] = link.get('href')
        i += 1
    return links
