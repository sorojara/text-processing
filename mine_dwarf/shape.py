from textwrap3 import wrap

def wrap_text_to_array(text, size):
	ret = wrap(text, size)
	return ret

def wrap_text(text, size):
	buffer_list = wrap(text, size)
	join_char = '\n'
	ret = join_char.join(buffer_list)
	return ret

def tokenize(text, separator):
	return text.split(separator)

def sort_tokens(tokens):
	tokens.sort()
	return tokens