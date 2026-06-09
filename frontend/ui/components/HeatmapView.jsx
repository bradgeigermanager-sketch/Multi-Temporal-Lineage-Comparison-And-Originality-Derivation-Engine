const HeatmapView = ({ data }) => {
  return (
    <div className="heatmap-container" aria-label="Originality Probability Heatmap">
      {data.map(item => (
        <div 
          key={item.id}
          style={{ 
            backgroundColor: `rgba(255, 165, 0, ${item.probability})`,
            width: '50px', height: '50px' 
          }}
          title={`Probability: ${item.probability}`}
        />
      ))}
    </div>
  );
};
