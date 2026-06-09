const AncestryForm = () => {
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/variations', { /* ... */ });
      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail); // "Circular dependency detected"
      }
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* ... inputs ... */}
      {error && (
        <div role="alert" aria-live="assertive" style={{ color: 'red' }}>
          <p><strong>Error:</strong> {error}</p>
        </div>
      )}
      <button type="submit">Commit to Lineage</button>
    </form>
  );
};
