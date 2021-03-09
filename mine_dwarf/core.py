from mine_dwarf.file import open_file
 
def read_file(file):
	print('Printing "{}"...'.format(file))
	print(open_file(file))