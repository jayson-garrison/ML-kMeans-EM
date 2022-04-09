import os
from Utils.Sample import Sample
from DocumentDistances.doc2vec_email import *
from DocumentDistances.doc2vec_psalms import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import lines


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

def load_psalms_as_samples(dims):
    k=2
    samples = []
    model = load_doc2vec_psalm_model(dims)

    rsvce_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsRSVCE.txt"
    rsvce_file = open(rsvce_path)
    for line in rsvce_file:
        words = line.split()
        label = 'rsvce'
        vector = model.infer_vector(words)
        sample = Sample(vector, np.random.randint(k), true_label=label)
        samples.append(sample)
    
    kjv_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsKJV.txt"
    kjv_file = open(kjv_path)
    for line in kjv_file:
        words = line.split()
        label = 'kjv'
        vector = model.infer_vector(words)
        sample = Sample(vector, np.random.randint(k), true_label=label)
        samples.append(sample)

    return samples


def visualize_psalms_in_3d():
    model = load_doc2vec_psalm_model(3)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    rsvce_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsRSVCE.txt"
    rsvce_file = open(rsvce_path)
    x1 = []
    y1 = []
    z1 = []
    for line in rsvce_file:
        words = line.split()
        label = 'rsvce'
        vector = model.infer_vector(words)
        x1.append(vector[0])
        y1.append(vector[1])
        z1.append(vector[2])
    ax.scatter(x1, y1, z1, marker='^', alpha=.05)
        
    kjv_path = os.getcwd() + "//project//Datasets//Psalms//PsalmsKJV.txt"
    kjv_file = open(kjv_path)
    x2 = []
    y2 = []
    z2 = []
    for line in kjv_file:
        words = line.split()
        label = 'kjv'
        vector = model.infer_vector(words)
        x2.append(vector[0])
        y2.append(vector[1])
        z2.append(vector[2])
    ax.scatter(x2, y2, z2, marker='o', alpha=.05)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    blue_triangles = lines.Line2D([], [], color='blue', marker='^', linestyle='None', label='RSVCE Verse Embeddings')
    orange_circles = lines.Line2D([], [], color='orange', marker='o', linestyle='None', label='KJV Verse Embeddings')
    plt.legend(handles=[blue_triangles, orange_circles])

    plt.show()

def visualize_psalm_test_results():
    path = os.getcwd() + "//project//DocumentDistances//Output//psalm_silhouette_scores.txt"
    file = open(path)
    xs = []
    ys = []
    for line in file:
        coords = line.split(' ')
        xs.append(int(coords[0]))
        ys.append(float(coords[1]))
    plt.plot(xs, ys)
    plt.xlabel("Embedding Dimensions")
    plt.ylabel("Silhouette Index")
    plt.show()
