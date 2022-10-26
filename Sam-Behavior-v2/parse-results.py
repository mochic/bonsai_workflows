import csv


def load_csv(path):
	with open(path, newline="") as f:
		reader = csv.reader(f, delimiter=',')
		columns = next(reader)
		mapping = {
			k: []
			for k in columns
		}
		for row in reader:
			for idx, value in enumerate(row):
				mapping[columns[idx]].append(value)
		return mapping


def get_go_nogo_counts(values):
	go_count = 0
	nogo_count = 0
	for value in values:
		if value == "GO":
			go_count += 1
		elif value == "NOGO":
			nogo_count += 1
		else:
			raise Exception("Unexpected value=%s" % value)
	return go_count, nogo_count


if __name__ == "__main__":
	loaded = load_csv("results.csv")
	print(loaded)
	go_count, nogo_count = get_go_nogo_counts(loaded["Value"])
	print("Go nogo percent: %s" % ((go_count / nogo_count) * 100))
	
	