









def test1():
    from sklearn.cluster import AffinityPropagation
    import numpy as np
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [4, 2], [4, 4], [4, 0]])
    clustering = AffinityPropagation().fit(X)
    clustering

    clustering.labels_

    clustering.predict([[0, 0], [4, 4]])

    clustering.cluster_centers_





if __name__ == "__main__":
    test1()