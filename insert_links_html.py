from dbconnect import connection

def getLinks():
	c,conn = connection()
	html_file = open('bbc_rssfeed.html','w+')
	c.execute('SELECT link FROM rss_links')
	rows = c.fetchall()
	loopCount=0
	rowCount = c.rowcount
	for row in rows:
		link_tag = '<a href="' + row[0] + '">' + row[0][26:] + '</a>'
		html_file.append(link_tag)
		loopCount = loopCount + 1
	conn.close()
	if loopCount == rowCount:
		return 1
	return 0

retcode = getLinks()
print('status' , 1)


