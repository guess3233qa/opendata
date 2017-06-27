import MySQLdb

class DBConn:

	def _init_(self):
		self.user="root"
                self.host="localhost"
                self.passwd="ttmaker"
                self.dbname="opendata"

	def dbConn(self):
		self.db=MySQLdb.connect(self.host,self.user,self.passwd,self.dbname,charset='utf8')
		self.cursor = self.db.cursor()

	def runQuery(self,sql):
		self.cursor.execute(sql)
		self.results=self.cursor.fetchall()

	def dbClose(self):
		self.db.close()

