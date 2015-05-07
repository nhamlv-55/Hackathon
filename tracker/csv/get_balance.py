import json
import urllib2
f = open("accounts.json", "r")
d = f.read()
f.close()
accounts = json.loads(d)

f = open("customer_with_geo.json", "r")
d= f.read()
f.close()
customers = json.loads(d)


# f = open("trans_graph.csv", "w")
# f.write("source,target\n")
for customer in customers:
	# print customer["_id"], "-------"
	customer["balance"] = 0
	for account in accounts:
		# print account["customer"]
		if account["customer"]==customer["_id"]:
			customer["balance"]+=account["balance"]
	print customer["balance"]

f = open("full_customer_record.json", "w")
f.writelines(json.dumps(customers))
f.close()


