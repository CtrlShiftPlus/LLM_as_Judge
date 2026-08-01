import ScoreCard from "./ScoreCard";
import JudgeCard from "./JudgeCard";
import Charts from "./Charts";

export default function Dashboard({ data }) {
	const judges = data?.judges || [];
	const consensus = data?.consensus || {};
	const master = data?.master_judge || {};
	const masterEvidence = master?.evidence
		? Array.isArray(master.evidence)
			? master.evidence
			: Object.entries(master.evidence).map(([key, value]) => `${key}: ${value}`)
		: [];
	const overall = consensus.overall_score ?? Math.round(
		judges.reduce((s, j) => s + (j.weighted_score || j.score || 0), 0)
	);

	return (
		<div>
			<ScoreCard score={overall} />

			<div className="grid">
				{judges.map((j, i) => (
					<JudgeCard key={i} judge={j} />
				))}
			</div>

			<Charts judges={judges.map((j) => ({ name: j.judge, score: j.score }))} />

			<div className="card">
				<h2>Consensus Summary</h2>
				{consensus.overall_status ? <p><strong>Status:</strong> {consensus.overall_status}</p> : null}
				{consensus.overall_risk ? <p><strong>Risk:</strong> {consensus.overall_risk}</p> : null}
				{consensus.overall_score != null ? <p><strong>Score:</strong> {consensus.overall_score}</p> : null}
				<p>{consensus.summary}</p>
				<p>
					<strong>Strengths:</strong> {consensus.strengths?.join(", ") || "None"}
				</p>
				<p>
					<strong>Weaknesses:</strong> {consensus.weaknesses?.join(", ") || "None"}
				</p>
				{consensus.recommendations?.length ? (
					<div className="recommendations">
						<strong>Recommendations:</strong>
						<ul>
							{consensus.recommendations.map((item, i) => (
								<li key={i}>{item}</li>
							))}
						</ul>
					</div>
				) : null}
			</div>

			<div className="card">
				<h2>Master Judge</h2>
				{master.overall_score != null ? <p><strong>Score:</strong> {master.overall_score}</p> : null}
				{master.score != null ? <p><strong>Score:</strong> {master.score}</p> : null}
				{master.status ? <p><strong>Status:</strong> {master.status}</p> : null}
				{master.risk ? <p><strong>Risk:</strong> {master.risk}</p> : null}
				<p>{master.summary ?? ""}</p>
				{master.strengths?.length ? <p><strong>Passed Models:</strong> {master.strengths.join(", ")}</p> : null}
				{master.weaknesses?.length ? <p><strong>Failed Models:</strong> {master.weaknesses.join(", ")}</p> : null}
				<p>
					<strong>Recommendation:</strong> {master.recommendation || "None"}
				</p>
				{masterEvidence.length ? (
					<div className="evidence">
						<strong>Evidence:</strong>
						<ul>
							{masterEvidence.map((e, i) => <li key={i}>{e}</li>)}
						</ul>
					</div>
				) : null}
			</div>
		</div>
	);
}