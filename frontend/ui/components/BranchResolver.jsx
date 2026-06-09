const BranchResolver = ({ branchA, branchB }) => (
  <div className="comparison-grid">
    <BranchPanel data={branchA} title="Lineage Branch A" />
    <div className="resolver-controls">
      <p>System Consensus: Branch A (65%) vs Branch B (35%)</p>
      <button onClick={() => resolve(branchA)}>Adopt Branch A</button>
      <button onClick={() => resolve(branchB)}>Adopt Branch B</button>
    </div>
    <BranchPanel data={branchB} title="Lineage Branch B" />
  </div>
);
