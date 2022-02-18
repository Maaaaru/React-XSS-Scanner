def file_scan(file_path):
	with open(file_path) as f:
		for line in f:
			line = line.rstrip()
			print(line)
