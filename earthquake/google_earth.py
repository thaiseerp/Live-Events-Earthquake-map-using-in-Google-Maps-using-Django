"""
Author: Thaiseer Parammal
"""

from . import function
import os
import re


def write_to_kml():
    directory = os.path.join(os.path.dirname(os.path.realpath('__file__')), 'earthquake\static\earthquake.kml')
    file = open(directory, 'w')
    title = function.gettitle()
    latlong = function.getlatlong()
    time = function.gettime()
    link = function.getlink()
    file.write('<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n')
    for i in range(1, len(title)):
        n_e = re.findall("[a-zA-Z]+", latlong[i])
        lt = re.findall("\d+\.\d+", latlong[i])
        lat = lt[0]
        long = lt[1]
        north = n_e[0]
        east = n_e[1]
        if north == 'S':
            lat = -1*float(lat)
        if east == 'W':
            long = -1*float(long)
        file.write(
                '<Placemark>\n'
                '<name>'+str(title[i])+'</name>\n'
                '<description>\n'
                '<![CDATA[\n'
                '<h2 style="color:#a90000">' + title[i] + '</h2><h4 style="color:#00a8bb">' + time[i] +
                '</h4><br /><h4 style="color:#00646f">For more details about this earthquake, '
                'click <a target="_blank" href="'
                + link[i] + '">here </a></h4>\n'
                ']]></description>\n'
                '<Point>\n'
                '<coordinates>'+str(long)+','+str(lat)+',0</coordinates>\n'
                '</Point>\n'
                '</Placemark>\n')
    file.write('</Document>\n</kml>')
    file.close()
