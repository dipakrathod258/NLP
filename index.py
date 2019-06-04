from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from bs4 import BeautifulSoup
import urllib.request
from nltk.corpus import stopwords

sr = stopwords.words('english')


response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
res = response.read()
soup = BeautifulSoup(res,'html5lib')
text = soup.get_text(strip = True)
# print(len(word_tokenize(text)))
tokens = [t for t in text.split()]
# print(lis)
x =len(tokens)

for token in tokens:
	if token in sr:
		tokens.remove(token)
freq = nltk.FreqDist(tokens)
for key, val in freq.items():
	print(str(key) +":"+ str(val))
freq.plot(20, cumulative=False)