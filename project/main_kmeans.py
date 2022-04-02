from Utils.miscellaneous import load_image_as_samples, load_gaussian_file_as_samples, visualize_gaussian_1d
from KMeans.kmeans import KMeans
import numpy as np
from matplotlib import pyplot
import os

def run_gaussian_test(theta):
    file_no = theta[0]
    num_clusters = theta[1]
    samples = load_gaussian_file_as_samples(file_no=file_no, k=num_clusters)

    # log the data
    data_file_name = f'project/KMeans/Output/Gaussian/Data/file{file_no}_clusters{num_clusters}.txt'
    os.makedirs(os.path.dirname(data_file_name), exist_ok=True)
    with open(data_file_name, 'w') as log:
        # Calc accuracies
        X = []
        Y = []
        for test in range(50):
            model = KMeans(samples=samples, k=num_clusters, dimensions=1)
            model.learn(C=2/len(samples))
            likelihood = model.evaluate_likelihood()
            X.append(test)
            Y.append(likelihood)
            log.write(str(test)+" "+str(likelihood)+"\n")
        # save a visualization of the data from the tests as a line plot
        pyplot.plot(X, Y)
        pyplot.xlabel("Test Number")
        pyplot.ylabel("Likelihood of Clusters")
        lineplot_file_name = f'project/KMeans/Output/Gaussian/LinePlots/file{file_no}_clusters{num_clusters}.jpg'
        os.makedirs(os.path.dirname(lineplot_file_name), exist_ok=True)
        pyplot.savefig(lineplot_file_name)
        pyplot.close()
        log.close()

    # save one visualization of estimated mean
    visual_file_name = f'project/KMeans/Output/Gaussian/ClusterVisuals/file{file_no}_clusters{num_clusters}.jpg'
    os.makedirs(os.path.dirname(visual_file_name), exist_ok=True)
    model = KMeans(samples=samples, k=num_clusters, dimensions=1)
    model.learn(C=2/len(samples))
    visualize_gaussian_1d(file_no=file_no, estimted_means=model.getCentroids(), save_path=visual_file_name, show=False)



if  __name__ == "__main__":
    run_gaussian_tests = True
    Theta_Gaussian = [
        # file_no, number_of_clusters, 
        # Experiment 1: ===============================================
        # pt 1
        (1, 2),
        (1, 3),
        (1, 6),
        (1, 8),
        (2, 2),
        (2, 3),
        (2, 6),
        (2, 8),
        (3, 2),
        (3, 3),
        (3, 6),
        (3, 8),
        (4, 2),
        (4, 3),
        (4, 6), 
        (4, 8),
        # pt 2
        (5, 5),
        (6, 5),
        (7, 5),
        (8, 5),
        # pt 3
        (9, 10),
        (10, 10),
        (11, 10),
        (12, 10),

        # Experiment 2: ===============================================
        (13, 5),
        (14, 5),
        (15, 5),

        # Experiment 3: ===============================================
        (16, 5),

        # Experiment 4: ===============================================
        (17, 5),
        (18, 5),
        (19, 5),
    ]

    if run_gaussian_tests:
        for theta in Theta_Gaussian:
            run_gaussian_test(theta)
            

    # samples = load_image_as_samples("Colors.jpg", k)

    
    
    # model.paint_by_numbers("TheLastSupper.jpg")
