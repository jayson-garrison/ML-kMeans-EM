import email
from pydoc import doc
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import get_tmpfile
import os


def build_doc2vec_email_model():
    emails = list()
    email_path = os.getcwd() + "//project//Datasets//Email//email_for_docs.txt"
    file = open(email_path)
    for line in file:
        emails.append(line.split(' '))
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(emails)]
    print('Training model')
    model = Doc2Vec(documents, vector_size=20, window=2, min_count=50, workers=4)
    save_path = os.getcwd() + "//project//DocumentDistances//doc2vecEMAIL.model"
    model.save(save_path)
    vector = model.infer_vector(["the", "am"])
    print(vector)

def load_doc2vec_email_model():
    load_path = os.getcwd() + "//project//DocumentDistances//doc2vecEMAIL.model"
    model = Doc2Vec.load(load_path)
    return model

