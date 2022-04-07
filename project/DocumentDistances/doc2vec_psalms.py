from pydoc import doc
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import get_tmpfile
import os


def build_doc2vec_psalm_model(dims):
    verses = list()
    
    rsvce_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsRSVCE.txt"
    rsvce_file = open(rsvce_path)
    for line in rsvce_file:
        verses.append(line.split(' '))
    
    kjv_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsKJV.txt"
    kjv_file = open(kjv_path)
    for line in kjv_file:
        verses.append(line.split())

    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(verses)]
    print('Training model')
    model = Doc2Vec(documents, vector_size=dims, window=2, min_count=3, workers=4)
    save_path = os.getcwd() + f"//project//DocumentDistances//Models//doc2vecPSALMS_{dims}.model"
    model.save(save_path)
    vector = model.infer_vector(["the", "am"])
    print(vector)

def load_doc2vec_psalm_model(dims):
    load_path = os.getcwd() + f"//project//DocumentDistances//Models//doc2vecPSALMS_{dims}.model"
    model = Doc2Vec.load(load_path)
    return model


# for dim in range(3, 30):
#     build_doc2vec_psalm_model(dim)
