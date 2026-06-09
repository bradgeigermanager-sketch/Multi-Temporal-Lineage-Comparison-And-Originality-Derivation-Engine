from fastapi import FastAPI
from neo4j import GraphDatabase

app = FastAPI()
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

@app.get("/calculate-original")
async def get_original_candidates():
    query = """
    MATCH (root:Variation)
    WHERE NOT (root)-[:EVOLVED_FROM]->()
    OPTIONAL MATCH (root)<-[:EVOLVED_FROM*]-(descendant)
    RETURN root.id AS id, count(descendant) AS reach
    ORDER BY reach DESC
    """
    with driver.session() as session:
        result = session.run(query)
        return [{"id": record["id"], "reach": record["reach"]} for record in result]
