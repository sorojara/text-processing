def open_file(file):
	try:
		with open(file, 'r') as f:
			data = f.read()
		return data
	except:
		raise Exception