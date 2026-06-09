// /frontend/src/components/FunnelExplorer.jsx
import React, { useState } from 'react';

const FunnelExplorer = ({ currentGroup }) => {
  const [history, setHistory] = useState([currentGroup]);

  const handleTighten = (childGroup) => {
    setHistory([...history, childGroup]);
    // Trigger API call to fetch child nodes
  };

  return (
    <nav role="navigation" aria-label="Funnel Breadcrumbs">
      <ol>
        {history.map((group, index) => (
          <li key={group.id}>
            <button onClick={() => setHistory(history.slice(0, index + 1))}>
              {group.name}
            </button>
          </li>
        ))}
      </ol>
      <div className="tightening-controls">
        <button onClick={() => handleTighten(nextGroup)}>Tighten Search</button>
      </div>
    </nav>
  );
};
