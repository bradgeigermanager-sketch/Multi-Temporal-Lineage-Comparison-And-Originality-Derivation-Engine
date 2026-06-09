import { ScatterChart, Scatter, XAxis, YAxis, Tooltip } from 'recharts';

const EntropyScatterPlot = ({ data }) => (
  <ScatterChart width={600} height={300} aria-label="Entropy Contribution Scatter Plot">
    <XAxis dataKey="depth" name="Lineage Depth" />
    <YAxis dataKey="entropy" name="Entropy Contribution" />
    <Tooltip cursor={{ strokeDasharray: '3 3' }} />
    <Scatter name="Variations" data={data} fill="#8884d8" />
  </ScatterChart>
);
