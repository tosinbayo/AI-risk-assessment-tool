type Props = {
  label: string;
  value: string;
};

export default function MetricCard({ label, value }: Props) {
  return (
    <div className="card">
      <div className="metric-value">{value}</div>
      <div className="metric-label" style={{ marginTop: 6 }}>{label}</div>
    </div>
  );
}
