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
