#coding=utf8
import MySQLdb

try:
	db = MySQLdb.connect(host="localhost",user="root",passwd="ttmaker",db="opendata",charset='utf8')
	sql = "select a.Location,b.Location from 00_HauntedHouse a join 00_RentHouses b join 03_WChild c on a.id=b.id=c.id"
	cursor=db.cursor()

	cursor.execute(sql)
	results = cursor.fetchall()

	for i in results:
		for j in  i:
			print j

	db.close()

except :
	print "Error"
