const TimelinePruner = ({ timelines, onPrune }) => (
  <div className="pruning-panel">
    <h3>Research Priority Queue</h3>
    {timelines.sort((a,b) => b.evidenceScore - a.evidenceScore).map(t => (
      <div key={t.id} className="timeline-row">
        <span>{t.name} (Score: {t.evidenceScore})</span>
        <button onClick={() => onPrune(t.id)}>Deprioritize</button>
      </div>
    ))}
  </div>
);
