from bs4 import BeautifulSoup
import time
import urllib.request
from dbconnect import connection

c, conn = connection()

def getPage():
    req = urllib.request.Request('http://feeds.bbci.co.uk/news/rss.xml')
    req = urllib.request.urlopen(req)
    xml = BeautifulSoup(req, 'lxml-xml')
    return xml

def getLinks(xml):
    for item in xml.find_all('link')[2:]:
        url = item.text
        print(url)
        c.execute('SELECT * FROM rss_links WHERE link = (%s)', (url))
        rows = c.fetchall()
        if len(rows) == 0:
            c.execute("INSERT INTO rss_links(time, link) VALUES(%s, %s)",
                      (time.time(), url))
            conn.commit()
            print('Found a new link', url)
        else:
            print('Link already exists in the database')
        time.sleep(10)
    conn.close()

while True:
    xml = getPage()
    getLinks(xml)
    time.sleep(30)
