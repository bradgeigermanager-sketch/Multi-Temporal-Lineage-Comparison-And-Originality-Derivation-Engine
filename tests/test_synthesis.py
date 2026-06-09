# /tests/test_synthesis.py
import pytest
from backend.services.synthesis import SynthesisEngine

def test_consensus_threshold_filtering():
    engine = SynthesisEngine(db_mock)
    # Test that nodes below 0.8 probability are excluded
    nodes = [{'id': 'v1', 'prob': 0.9}, {'id': 'v2', 'prob': 0.7}]
    consensus = engine.filter_nodes(nodes, threshold=0.8)
    assert len(consensus) == 1
    assert consensus[0]['id'] == 'v1'

def test_cycle_detection_on_reconstruction():
    engine = SynthesisEngine(db_mock)
    # Test that circular dependency triggers an error
    nodes = [{'id': 'v1', 'parent': 'v2'}, {'id': 'v2', 'parent': 'v1'}]
    with pytest.raises(ValueError, match="Cyclic dependency"):
        engine.reconstruct_graph(nodes)
