from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_variations(variations):
    # Vectorize the content of the variations
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([v.content for v in variations])
    
    # Cluster into groups
    kmeans = KMeans(n_clusters=3).fit(X)
    return kmeans.labels_
