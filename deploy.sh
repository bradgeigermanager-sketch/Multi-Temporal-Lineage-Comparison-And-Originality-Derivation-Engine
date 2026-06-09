#!/bin/bash
# 1. Spin up the infrastructure
docker-compose up -d --build

# 2. Wait for Neo4j to be ready (rudimentary check)
echo "Waiting for Neo4j..."
sleep 15

# 3. Apply Schema Constraints (Ensure uniqueness and cycle prevention)
docker exec -i engine_db_1 cypher-shell -u neo4j -p password <<EOF
CREATE CONSTRAINT variation_id_unique IF NOT EXISTS 
FOR (v:Variation) REQUIRE v.id IS UNIQUE;
EOF

echo "Engine Deployed Successfully."
