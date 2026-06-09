import networkx as nx

def identify_original_state(edges):
    # Create a Directed Graph
    G = nx.DiGraph()
    G.add_edges_from(edges)
    
    # 1. Identify roots (nodes with no ancestors)
    roots = [n for n, d in G.in_degree() if d == 0]
    
    # 2. Identify the node with the highest out-degree (most "descendants")
    out_degrees = dict(G.out_degree())
    most_likely_original = max(out_degrees, key=out_degrees.get)
    
    return roots, most_likely_original

# Example usage:
# (Variation_B -> Variation_C means B is the ancestor)
edges = [('A', 'B'), ('B', 'C'), ('A', 'D'), ('D', 'E')]
roots, best_match = identify_original_state(edges)
print(f"Ancestral Roots: {roots}, Most likely original: {best_match}")
