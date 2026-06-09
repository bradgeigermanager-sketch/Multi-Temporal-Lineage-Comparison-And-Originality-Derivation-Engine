const LineageListView = ({ variations }) => (
  <table aria-label="Historical Lineage Table">
    <thead>
      <tr>
        <th scope="col">Variation ID</th>
        <th scope="col">Ancestor ID</th>
        <th scope="col">Seniority Score</th>
        <th scope="col">Verified</th>
      </tr>
    </thead>
    <tbody>
      {variations.map((v) => (
        <tr key={v.id}>
          <td>{v.id}</td>
          <td>{v.parent_id || "Root"}</td>
          <td>{v.score.toFixed(2)}</td>
          <td>{v.is_verified ? "Yes" : "No"}</td>
        </tr>
      ))}
    </tbody>
  </table>
);
