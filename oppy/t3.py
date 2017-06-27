#coding=utf8
import MySQLdb

try:
	db = MySQLdb.connect(host="localhost",user="root",passwd="ttmaker",db="opendata",charset='utf8')

	table = ["00_HauntedHouse","00_RentHouses","01_FireBrigade","01_PoliceStation","02_CVS","02_ExcellentMarket","02_HardwareRetail","02_HardwareStore","02_Restaurant","03_WChild"]

	pX = raw_input("請輸入經度: ")
	pY = raw_input("請輸入緯度: ")

	cursor=db.cursor()

	sql = "select Location from 01_FireBrigade where Point_X like " + pX + " and Point_Y like " + pY
	print ("sql: ") + sql

	cursor.execute(sql)
	results = cursor.fetchall()

	for i in results:
		for j in i:
			print j


	db.close()

except :
	print "Error"
