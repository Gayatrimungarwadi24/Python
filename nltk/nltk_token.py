import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
#nltk.download('punkt_tab')

text="Hello World! How are you?"
words=word_tokenize(text)
print(words)
sentences=sent_tokenize(text)
print(sentences)