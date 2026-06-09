const SideBySideResolver = ({ nodeA, nodeB, onResolve }) => (
  <div className="resolver-grid" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr' }}>
    <div className="node-pane">
      <h3>Candidate A</h3>
      <p>Source Reliability: {nodeA.source_reliability}</p>
      <button onClick={() => onResolve(nodeA.id)}>Select as Original</button>
    </div>
    <div className="node-pane">
      <h3>Candidate B</h3>
      <p>Source Reliability: {nodeB.source_reliability}</p>
      <button onClick={() => onResolve(nodeB.id)}>Select as Original</button>
    </div>
  </div>
);
