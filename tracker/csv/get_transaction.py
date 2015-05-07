import json
import urllib2
f = open("accounts.json", "r")
d = f.read()
f.close()
accounts = json.loads(d)

f = open("trans.json", "r")
d= f.read()
f.close()
transactions = json.loads(d)


f = open("trans_graph.csv", "w")
f.write("source,target\n")
for transaction in transactions:
	payer = transaction["payer id"]
	payee = transaction["payee id"]
	for account in accounts:
		if account["_id"]==payer:
			payer_customer = account["customer"]
		if account["_id"]==payee:
			payee_customer = account["customer"]
	print payer, payer_customer, payee, payee_customer
	f.write(payer_customer)
	f.write(",")
	f.write(payee_customer)
	f.write("\n")

