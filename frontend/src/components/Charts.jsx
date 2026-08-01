import {
	ResponsiveContainer,
	BarChart,
	Bar,
	XAxis,
	YAxis,
	CartesianGrid,
	Tooltip,
	Legend,
	PieChart,
	Pie,
	Cell
} from "recharts";

export default function Charts({ judges }) {
	const data = judges.map((j) => ({ name: j.name, score: j.score }));
	const colors = ["#5b8cff", "#7ee0a8", "#ffb479", "#f77", "#b39cff"];

	return (
		<div className="charts-grid">
			<div className="chart">
				<h2>Judge Scores</h2>
				<ResponsiveContainer width="100%" height={320}>
					<BarChart data={data} margin={{ right: 20, left: 0 }}>
						<CartesianGrid strokeDasharray="3 3" stroke="#1c2a45" />
						<XAxis dataKey="name" tick={{ fill: "#cbd5ff" }} />
						<YAxis tick={{ fill: "#cbd5ff" }} />
						<Tooltip contentStyle={{ backgroundColor: "#0f172a", borderColor: "#2f4368", color: "#e8f0ff" }} />
						<Legend wrapperStyle={{ color: "#c8d4f6" }} />
						<Bar dataKey="score" radius={[10, 10, 0, 0]}>
							{data.map((_, i) => (
								<Cell key={`cell-${i}`} fill={colors[i % colors.length]} />
							))}
						</Bar>
					</BarChart>
				</ResponsiveContainer>
			</div>

			<div className="chart">
				<h2>Score Distribution</h2>
				<ResponsiveContainer width="100%" height={320}>
					<PieChart>
						<Pie data={data} dataKey="score" nameKey="name" outerRadius={110} label>
							{data.map((_, i) => (
								<Cell key={`pie-${i}`} fill={colors[i % colors.length]} />
							))}
						</Pie>
						<Tooltip contentStyle={{ backgroundColor: "#0f172a", borderColor: "#2f4368", color: "#e8f0ff" }} />
					</PieChart>
				</ResponsiveContainer>
			</div>
		</div>
	);
}