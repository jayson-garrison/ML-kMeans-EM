import os
from Utils.Sample import Sample
from DocumentDistances.doc2vec_email import *
import numpy as np


def load_email_as_samples():
    k=2
    email_path = os.getcwd() + "//project//Datasets//Email//email_for_docs.txt"
    file = open(email_path)
    model = load_doc2vec_email_model()

    samples=[]
    for line in file:
        words = line.split(' ')
        label="Ham"
        if words[-1] == "Prediction": label="Spam"
        vector =  model.infer_vector(words)
        sample = Sample(vector, np.random.randint(k), true_label=label)
        samples.append(sample)
    return samples

