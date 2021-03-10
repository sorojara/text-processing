import mine_dwarf.file as dwarfile
import mine_dwarf.shape as dwarfshape

def test_me(file, size):
	print('Wrapping "{}" to size {}'.format(file, size))
	print('\nOriginal text:')
	original_text = dwarfile.open_file(file)
	print(original_text)
	print('\nWrapped text:')
	wrapped_text = dwarfshape.wrap_text(original_text, size)
	print(wrapped_text)

 
def read_file(file):
	print('Printing "{}"...'.format(file))
	print(dwarfile.open_file(file))

def sort_file(file):
	print('Sorting "{}" lines'.format(file))
	print(dwarfile.sort_file_lines(file))

def wrap_file(file, size):
	print('Wrapping "{}" to size {}'.format(file, size))
	print('\nOriginal text:')
	original_text = dwarfile.open_file(file)
	print(original_text)
	print('\nWrapped text:')
	wrapped_text = dwarfshape.wrap_text(original_text, size)
	print(wrapped_text)