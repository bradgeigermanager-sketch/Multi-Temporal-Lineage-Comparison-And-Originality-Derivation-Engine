const WeightingForm = ({ variationId, onUpdate }) => {
  const [reliability, setReliability] = useState(0.5);

  const handleSubmit = async () => {
    await fetch(`/api/variations/${variationId}/reweight`, {
      method: 'POST',
      body: JSON.stringify({ reliability }),
    });
    onUpdate(); // Triggers a graph re-fetch
  };

  return (
    <div aria-labelledby="weight-title">
      <h3 id="weight-title">Adjust Source Reliability</h3>
      <label htmlFor="range">Confidence Score: {reliability}</label>
      <input 
        id="range" type="range" min="0" max="1" step="0.01" 
        value={reliability} onChange={(e) => setReliability(e.target.value)}
      />
      <button onClick={handleSubmit}>Update Likelihood</button>
    </div>
  );
};
