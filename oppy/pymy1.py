#coding=utf8
import MySQLdb

try:
	db = MySQLdb.connect(host="localhost",user="root",passwd="ttmaker",db="opendata",charset='utf8')
	sql = "select*from 00_HauntedHouse"
	cursor=db.cursor()

	cursor.execute(sql)
	results = cursor.fetchall()


	for record in results:
		print (record[0])
		print (record[1])
		print (record[2])
		print (record[3])

	db.close()

except :
	print ("Error")
