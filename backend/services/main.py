from fastapi import FastAPI, HTTPException
from neo4j import GraphDatabase
import os

app = FastAPI()
db_uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
driver = GraphDatabase.driver(db_uri, auth=("neo4j", "password"))

@app.post("/variations")
async def add_variation(data: dict):
    # Validation: Prevent circular dependency
    query_validate = """
    MATCH (a:Variation {id: $aid}), (d:Variation {id: $did})
    RETURN exists((d)-[:EVOLVED_FROM*]->(a)) AS is_ancestor
    """
    with driver.session() as session:
        # Execute logic to add node and link it if parent_id exists
        # ... logic to insert node and link ...
        pass
    return {"status": "success"}

@app.get("/calculate-original")
async def get_original():
    query = """
    MATCH (root:Variation)
    WHERE NOT (root)-[:EVOLVED_FROM]->()
    OPTIONAL MATCH (root)<-[:EVOLVED_FROM*]-(descendant)
    WITH root, count(descendant) AS reach, 
         datetime().epochMillis - root.created_at AS age
    RETURN root.id AS CandidateOriginal, 
           (reach * 0.7) + (log(age + 1) * 0.3) AS SeniorityScore
    ORDER BY SeniorityScore DESC
    """
    with driver.session() as session:
        result = session.run(query)
        return [{"id": r["CandidateOriginal"], "score": r["SeniorityScore"]} for r in result]
