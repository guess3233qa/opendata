#coding=utf8
import requests
import json

req = requests.get("http://10.1.72.74:8000/api/Renthouses/")
A = req.json()			#變list
B = json.dumps(A,indent=2)	#變str 分行空2格
C = json.loads(B)		#從str回原貌(list)


print (B)
print (type(B))

