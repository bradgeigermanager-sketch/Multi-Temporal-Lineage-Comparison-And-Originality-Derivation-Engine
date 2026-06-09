const TriangulationScoreboard = ({ branchAData, branchBData }) => (
  <div className="triangulation-card" role="region" aria-label="Triangulation Analysis">
    <h4>External Validation Strength</h4>
    <dl>
      <dt>Branch A Cross-Refs</dt>
      <dd>{branchAData.external_refs.length} sources</dd>
      <dt>Branch B Cross-Refs</dt>
      <dd>{branchBData.external_refs.length} sources</dd>
    </dl>
    <p>
      {branchAData.score > branchBData.score 
        ? "Branch A has stronger external anchoring." 
        : "Branch B has stronger external anchoring."}
    </p>
  </div>
);
