from Utils.miscellaneous import *
#from KMeans.kmeans import KMeans
from EM.em import ExpectationMaximization
import numpy as np
from matplotlib import pyplot
import os

def run_gaussian_test(theta):
    file_no = theta[0]
    num_clusters = theta[1]
    samples = load_gaussian_file_as_samples(file_no=file_no, k=num_clusters, linux=True)

    if False:

        # log the data
        data_file_name = f'project/EM/Output/Gaussian/Data/file{file_no}_clusters{num_clusters}.txt'
        os.makedirs(os.path.dirname(data_file_name), exist_ok=True)

    
        with open(data_file_name, 'w') as log:
            # Calc accuracies
            X = []
            Y = []
            for test in range(50):

                model = ExpectationMaximization(samples, num_clusters)
                model.learn(10)
                likelihood = model.evaluate_likelihood()

                X.append(test)
                Y.append(likelihood)
                log.write(str(test)+" "+str(likelihood)+"\n")
            # save a visualization of the data from the tests as a line plot
            pyplot.plot(X, Y)
            pyplot.xlabel("Test Number")
            pyplot.ylabel("Likelihood of Clusters")
            lineplot_file_name = f'project/EM/Output/Gaussian/LinePlots/file{file_no}_clusters{num_clusters}.jpg'
            os.makedirs(os.path.dirname(lineplot_file_name), exist_ok=True)
            pyplot.savefig(lineplot_file_name)
            pyplot.close()
            log.close()

    # save one visualization of estimated mean
    visual_file_name = f'project/EM/Output/Gaussian/ClusterVisuals/file{file_no}_clusters{num_clusters}.jpg'
    os.makedirs(os.path.dirname(visual_file_name), exist_ok=True)

    # model = KMeans(samples=samples, k=num_clusters, dimensions=1)
    # model.learn(C=2/len(samples))
    model = ExpectationMaximization(samples, num_clusters)
    model.learn(25)

    visualize_gaussian_1d(file_no=file_no, estimted_means=model.getMeans(), save_path=visual_file_name, show=False, linux=True)
    print(f'estimated means: {model.getMeans()}')

def run_image_test(theta):
    img_name = theta[0] + ".jpg"
    num_clusters = theta[1]
    samples = load_image_as_samples(img_name, num_clusters)
    img_output_name = f'project/KMeans/Output/Images/{theta[0]}_clusters{num_clusters}.jpg'
    os.makedirs(os.path.dirname(img_output_name), exist_ok=True)

    # Compress the image
    model = KMeans(samples=samples, k=num_clusters, dimensions=3)
    model.learn(C=2/len(samples))
    model.paint_by_numbers(img_name, save_path=img_output_name, show=False)


def run_iris_test(theta):
    metric = theta
    num_clusters = 3
    samples = load_iris_data_as_samples(num_clusters)
    # Cluster the iris data
    model = KMeans(samples=samples, k=num_clusters, dimensions=4)
    model.learn(C=2/len(samples))
    # Evaluate based on the metric
    result = 0
    clusters = model.getClusters()
    centroids = model.getCentroids()
    if metric == 'SSE':
        for idx in range(len(centroids)):
            result += sum_squared_errors(clusters[idx].getX(), centroids[idx])
        print(f'{metric}: {result}')
        return result
    elif metric == 'Silhouette':
        # NOTE: 1 is the best, -1 is the worst
        result = silhouette(clusters, centroids)
        print(f'{metric}: {result}')
        return result
    elif metric == 'Dunn':
        # NOTE: larger dunn index is better
        result = dunn(clusters)
        print(f'{metric}: {result}')
        return result



if  __name__ == "__main__":
    run_gaussian_tests = True
    run_image_tests = False
    run_iris_tests = False

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
        test_debug = False
        if test_debug:
            run_gaussian_test(Theta_Gaussian[1])
            exit()
            
        for theta in Theta_Gaussian:
            run_gaussian_test(theta)

    Theta_Image = [
        # ('Guadalupe', 3),
        # ('OurLadyOfMercy', 3),
        # ('DivineMercy', 3),
        # ('TheCoronation', 3),
        # ('TheCrucifixion', 3),
        # ('TheVirginAdoring', 3),
        # ('Guadalupe', 5),
        # ('OurLadyOfMercy', 5),
        # ('DivineMercy', 5),
        # ('TheCoronation', 5),
        # ('TheCrucifixion', 5),
        # ('TheVirginAdoring', 5),
        ('Guadalupe', 10),
        ('OurLadyOfMercy', 10),
        ('DivineMercy', 10),
        ('TheCoronation', 10),
        ('TheCrucifixion', 10),
        ('TheVirginAdoring', 10),
    ]
    if run_image_tests:
        for theta in Theta_Image:
            run_image_test(theta)
            
    Iris_Theta = [
        'SSE',
        'Silhouette',
        'Dunn'
    ]
    if run_iris_tests:
        for theta in Iris_Theta:
            run_iris_test(theta)