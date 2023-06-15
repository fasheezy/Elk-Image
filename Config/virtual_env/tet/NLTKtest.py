import nltk 
from nltk.tokenize import word_tokenize 
nltk.download('punkt')
text = "What is the meaning of this I am trying to escape and you bring me back"
print(word_tokenize(text))
