from bs4 import BeautifulSoup
import time
import urllib.request
from dbconnect import connection

req = urllib.request.urlopen('https://moz.com/top500')

xml = BeautifulSoup(req, 'html.parser')
c, conn = connection()
linksTable = xml.find_all('table')[0]; 
for item in xml.find_all('a')[24:44]:
    url = item.get('href')
    c.execute('SELECT * FROM links WHERE link = (%s)', (url))
    rows = c.fetchall()
    if len(rows) == 0:
        c.execute("INSERT INTO links(time, link) VALUES(%s, %s)",
                  (time.time(), url))
        conn.commit()
        print('Found a new link', url)
    else:
        print('Link already exists in the database')

conn.close()
