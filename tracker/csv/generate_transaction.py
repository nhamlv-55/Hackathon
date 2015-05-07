import json
import urllib2
from random import randint
f = open("accounts.json", "r")
d = f.read()
f.close()
accounts = json.loads(d)

# f = open("trans.json", "r")
# d= f.read()
# f.close()
# transactions = json.loads(d)


f = open("trans_graph2.csv", "w")
f.write("source,target\n")

for i in range(len(accounts)):
	if accounts[i]["balance"]>0:
		for j in range(10):
			print i	
			seed = randint(i, len(accounts)-1)
			x = randint(0,1)
			if(x==0):
				f.write(accounts[i]["customer"])
				f.write(",")
				f.write(accounts[seed]["customer"])
				f.write("\n")
# for transaction in transactions:
# 	payer = transaction["payer id"]
# 	payee = transaction["payee id"]
# 	for account in accounts:
# 		if account["_id"]==payer:
# 			payer_customer = account["customer"]
# 		if account["_id"]==payee:
# 			payee_customer = account["customer"]
# 	print payer, payer_customer, payee, payee_customer
# 	f.write(payer_customer)
# 	f.write(",")
# 	f.write(payee_customer)
# 	f.write("\n")

