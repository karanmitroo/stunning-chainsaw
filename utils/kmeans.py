import numpy as np
from sklearn.cluster import KMeans

def k_means(k, data):
    points = np.array(data, dtype=float)
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(points)
    unique, counts = np.unique(kmeans.labels_, return_counts=True)
    # print kmeans.labels_,
    # print "Intertia", kmeans.inertia_ 
    # print kmeans.predict(data)
    return dict(zip(unique, counts)), kmeans.inertia_