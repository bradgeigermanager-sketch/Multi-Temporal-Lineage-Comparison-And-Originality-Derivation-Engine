from fastapi import HTTPException

async def validate_ancestry(ancestor_id: str, descendant_id: str):
    # Check if the path exists to prevent circular loops
    query = """
    MATCH (a:Variation {id: $aid}), (d:Variation {id: $did})
    RETURN exists((d)-[:EVOLVED_FROM*]->(a)) AS is_ancestor
    """
    # If is_ancestor is True, the descendant is already an ancestor of the target, 
    # preventing a circular reference.
    if is_ancestor:
        raise HTTPException(status_code=400, detail="Circular dependency detected.")
