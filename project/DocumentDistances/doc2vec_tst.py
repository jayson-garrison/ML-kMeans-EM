from pydoc import doc
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import get_tmpfile

print(f'creating docs')
print(common_texts)
documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]
print(len(documents))
print(f'training model')
model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)
print(f'saving model')
fname = get_tmpfile("my_doc2vec_model")
model.save(fname)
print(f'loading model')
model = Doc2Vec.load(fname) 
print(f'testing')
vector = model.infer_vector(["system", "response"])
print(vector)
