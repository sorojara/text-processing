import mine_dwarf.file as dwarfile
import mine_dwarf.shape as dwarfshape
import mine_dwarf.calc as dwarfcalc
import mine_dwarf.nlp as dwarfnlp


def test_me(file, size):
	print('Count words in "{}"'.format(file))
	print('\nOriginal text:')
	original_text = dwarfile.open_file(file)
	print(original_text)
	words = dwarfshape.tokenize(original_text,' ')
	words_nlp = dwarfnlp.word_tokenize(original_text)
	print('\nWords Counted with split: {}'.format(dwarfcalc.count_tokens(words)))
	print('\nWords Counted with nlp: {}'.format(dwarfcalc.count_tokens(words_nlp)))

 
def read_file(file):
	print('Printing "{}"...'.format(file))
	print(dwarfile.open_file(file))

def sort_file(file):
	text = dwarfile.open_file_lines(file)
	print('Sorting "{}" lines'.format(file))
	print(dwarfshape.sort_tokens(text))

def wrap_file(file, size):
	print('Wrapping "{}" to size {}'.format(file, size))
	print('\nOriginal text:')
	original_text = dwarfile.open_file(file)
	print(original_text)
	print('\nWrapped text:')
	wrapped_text = dwarfshape.wrap_text(original_text, size)
	print(wrapped_text)