def calculate_originality_probability(node):
    # node.centrality: how many paths flow through/from it
    # node.contradictions: how many conflicting data points it resolves
    # node.age: temporal distance from the start of the study
    
    score = (node.centrality * 0.4) + (node.contradictions * 0.4) + (node.age * 0.2)
    return score
