from DocumentDistances.misc import load_email_as_samples, load_psalms_as_samples, visualize_psalms_in_3d, visualize_psalm_test_results
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

def run_psalm_test(theta):
    num_clusters = 2
    print('Loading samples')
    samples = load_psalms_as_samples(theta) # NOTE: takes about 30 seconds to load all of the email samples
    print('Clustering verses')
    # Cluster the email data
    model = KMeans(samples=samples, k=num_clusters, dimensions=theta)
    model.learn(C=2/len(samples))
    # Evaluate based on the metric
    print('Evaluating model')
    result = 0
    clusters = model.getClusters()
    centroids = model.getCentroids()

    result = silhouette(clusters, centroids)
    print(f'Silhouette on Psalms with {theta} dims: {result}')
    return result

if __name__ == "__main__":
    run_email_tests = False
    run_psalm_tests = False
    show_psalm_cluster_visuals = False
    show_psalm_test_results = True

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
    
    if run_psalm_tests:
        out_path = os.getcwd() + "//project//DocumentDistances//Output//psalm_silhouette_scores.txt"
        file = open(out_path, 'w')
        for theta in range(3, 30):
            result = run_psalm_test(theta)
            file.write(f'{theta} {result} \n')

    if show_psalm_cluster_visuals:
        visualize_psalms_in_3d()

    if show_psalm_test_results:
        visualize_psalm_test_results()


