def open_file(file):
	try:
		with open(file, 'r') as f:
			data = f.read()
		return data
	except:
		raise Exception

def open_file_lines(file):
	try:
		with open(file, 'r') as f:
			data = f.readlines()
		return data
	except:
		raise Exception

def open_sorted_file_lines(file):
	ret = open_file_lines(file)
	ret.sort()
	return ret