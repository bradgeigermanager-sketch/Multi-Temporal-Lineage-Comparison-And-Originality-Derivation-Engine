import numpy as np
from scipy.stats import entropy

def calculate_system_entropy(feature_vectors):
    """Calculates the Shannon entropy of the dataset."""
    # Convert features to a probability distribution
    counts = np.bincount(feature_vectors)
    probs = counts / len(feature_vectors)
    return entropy(probs, base=2)

def detect_outliers_by_entropy(feature_vectors):
    """Identifies outliers by finding nodes that maximize system disorder."""
    baseline_entropy = calculate_system_entropy(feature_vectors)
    anomaly_scores = []
    
    for i in range(len(feature_vectors)):
        # Create a subset excluding index i
        subset = np.delete(feature_vectors, i)
        subset_entropy = calculate_system_entropy(subset)
        
        # Anomaly score: How much does entropy drop when i is removed?
        anomaly_scores.append(baseline_entropy - subset_entropy)
        
    return np.array(anomaly_scores)
