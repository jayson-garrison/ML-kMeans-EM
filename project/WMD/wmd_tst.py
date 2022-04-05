from nltk.corpus import stopwords
from nltk import download
from pyemd import emd
from gensim.similarities import WmdSimilarity
import gensim.downloader as api


print(f'Loading stop words')
# download('stopwords')  # Download stopwords list.
stop_words = stopwords.words('english')

def preprocess(sentence):
    return [w for w in sentence.lower().split() if w not in stop_words]

sentence_obama = 'Obama speaks to the media in Illinois'
sentence_president = 'The president greets the press in Chicago'

sentence_obama = preprocess(sentence_obama)
sentence_president = preprocess(sentence_president)

print(f'Loading word2vec model')
model = api.load('word2vec-google-news-300')

print(f'Calculating wmdistance')
distance = model.wmdistance(sentence_obama, sentence_president)
print('distance = %.4f' % distance)

sentence_orange = preprocess('Oranges are my favorite fruit')
distance = model.wmdistance(sentence_obama, sentence_orange)
print('distance = %.4f' % distance)