pred = open("predsubmit.csv", "r")
mapping = open("map.csv", "r")

concat = open("model3.csv", "w")

pred_data = pred.readlines()
mapping_data = mapping.readlines()

for i in range(len(pred_data)):
	print pred_data[i]
	index, value = pred_data[i].strip().split(",")
	print mapping_data[i]
	module, component, year, month = mapping_data[i].strip().split(",")

	line = ",".join([module, component, year, month, value])
	concat.write(line)
	concat.write("\n")