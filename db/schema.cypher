// Ensure unique identifiers for nodes
CREATE CONSTRAINT variation_id_unique IF NOT EXISTS FOR (v:Variation) REQUIRE v.id IS UNIQUE;
CREATE CONSTRAINT timeline_id_unique IF NOT EXISTS FOR (t:Timeline) REQUIRE t.id IS UNIQUE;
CREATE CONSTRAINT group_id_unique IF NOT EXISTS FOR (g:PatternGroup) REQUIRE g.id IS UNIQUE;

// Ensure provenance dates are indexed for time-based queries
CREATE INDEX variation_created_idx IF NOT EXISTS FOR (v:Variation) ON (v.created_at);

// Ensure no node evolves from its own descendants (Cycle Prevention)
CALL apoc.trigger.add('check-cycle', 
"UNWIND $createdRelationships AS rel
 MATCH (start)-[:EVOLVED_FROM*]->(end)
 WHERE id(start) = id(end)
 CALL apoc.util.validate(true, 'Cyclic dependency detected in lineage', [id(start)])
 RETURN count(*)", 
{phase: 'before'});

// Trigger to log all 'Synthesis' events
CALL apoc.trigger.add('audit-synthesis',
"UNWIND $createdNodes AS node
 WITH node WHERE node:Synthesized
 CREATE (a:Audit {action: 'SYNTHESIS', timestamp: datetime(), target: id(node)})
 CREATE (a)-[:PERFORMED_BY]->(u:User {id: $user_id})",
{phase: 'after'});

// Procedure to create a new GroupEntry and link it to the previous narrowing level
CREATE (newGroup:PatternGroup {
    id: $new_id, 
    threshold: $threshold, 
    created_at: datetime()
})
WITH newGroup
MATCH (parent:PatternGroup {id: $parent_id})
CREATE (newGroup)-[:NARROWED_FROM]->(parent)
WITH newGroup
MATCH (t:Timeline)
WHERE t.structural_signature IN $subset
CREATE (t)-[:BELONGS_TO]->(newGroup)
RETURN newGroup.id;
