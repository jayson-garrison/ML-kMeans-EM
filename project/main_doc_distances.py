from DocumentDistances.misc import load_email_as_samples
from KMeans.kmeans import KMeans
from Utils.miscellaneous import *

def run_email_test(thetas):
    num_clusters = 2
    print('Loading samples')
    samples = load_email_as_samples() # NOTE: takes about 30 seconds to load all of the email samples
    print('Clustering emails')
    # Cluster the email data
    model = KMeans(samples=samples, k=num_clusters, dimensions=20)
    model.learn(C=2/len(samples))
    # Evaluate based on the metric
    print('Evaluating model')
    result = 0
    clusters = model.getClusters()
    centroids = model.getCentroids()
    for theta in thetas:
        metric = theta
        if metric == 'SSE':
            for idx in range(len(centroids)):
                result += sum_squared_errors(clusters[idx].getX(), centroids[idx])
            print(f'{metric}: {result}')
        elif metric == 'Silhouette':
            # NOTE: 1 is the best, -1 is the worst
            result = silhouette(clusters, centroids)
            print(f'{metric}: {result}')
        elif metric == 'Dunn':
            # NOTE: larger dunn index is better
            result = dunn(clusters)
            print(f'{metric}: {result}')



if __name__ == "__main__":
    run_email_tests = True

    Theta_Email = [
        'SSE',
        'Silhouette',
        'Dunn'
    ]
    if run_email_tests:
        run_email_test(Theta_Email)
        # SSE: 17519.482332076706
        # Silhouette: 0.8158002975407769
        # Dunn: 0.00761659146129888