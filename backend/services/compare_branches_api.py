@app.get("/compare-branches")
async def compare_branches(root_a: str, root_b: str):
    query = """
    MATCH (rootA:Variation {id: $rootA}), (rootB:Variation {id: $rootB})
    OPTIONAL MATCH (rootA)<-[:EVOLVED_FROM*]-(descA)
    OPTIONAL MATCH (rootB)<-[:EVOLVED_FROM*]-(descB)
    RETURN collect(distinct descA) AS branchA, collect(distinct descB) AS branchB
    """
    with driver.session() as session:
        result = session.run(query, rootA=root_a, rootB=root_b)
        # Logic to return serialized tree structures
        return result.data()
