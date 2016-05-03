from nltk.corpus import gutenberg
import nltk
print gutenberg.fileids()
texts = gutenberg.words('shakespeare-hamlet.txt')
