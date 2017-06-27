#coding=UTF8
#import DB
import MySQLdb
from dbconn import DBConn

try:
	dbuse = DBConn()
	dbuse.dbConnect()

	sql="select*from 02_CVS"
	dbuse.runQuery(sql)
	results = dbuse.results

	for i in results:
		for j in i:
			print j

	dbuse.dbClose()

except:
	print "MySQL DB Error"
