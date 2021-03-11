import nltk
nltk.download('punkt')

import mine_dwarf.shape as dwarfshape

def word_tokenize(text):
    return nltk.word_tokenize(text)

def line_tokenize(text):
    return dwarfshape.tokenize(original_text,'\n')

def line_access(text, index):
    lines = line_tokenize(text)[index]

def token_access(tokens, index):
    lines = tokens[index]