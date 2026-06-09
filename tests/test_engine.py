import pytest
from backend.analysis import calculate_likelihood, calculate_system_entropy

def test_likelihood_normalization():
    candidates = [{'id': 'A', 'score': 0.8}, {'id': 'B', 'score': 0.2}]
    normalized = normalize_scores(candidates)
    assert sum(c['probability'] for c in normalized) == pytest.approx(1.0)

def test_entropy_anomaly_detection():
    # Dataset with a clear outlier
    vectors = [1, 1, 1, 1, 1, 5] 
    scores = detect_outliers_by_entropy(vectors)
    # The outlier (index 5) should have the highest anomaly score
    assert np.argmax(scores) == 5
