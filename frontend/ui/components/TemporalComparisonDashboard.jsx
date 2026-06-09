const TemporalDashboard = ({ timeSlices }) => (
  <div className="temporal-analysis">
    <TimelineScrubber onChange={updateSlice} />
    <GrowthChart data={timeSlices} />
    <StructuralSunburst data={timeSlices.current} />
  </div>
);
