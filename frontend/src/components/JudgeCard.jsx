export default function JudgeCard({ judge }) {
  const name = judge?.judge || judge?.name || "Judge";
  const score = judge?.score ?? "N/A";
  const status = judge?.status ?? (typeof score === "number" && score >= 85 ? "PASS" : "WARNING");
  const risk = judge?.risk ?? "N/A";
  const confidenceRaw = judge?.confidence;
  let confidence = "N/A";
  if (confidenceRaw != null) {
    if (typeof confidenceRaw === "number") {
      confidence = confidenceRaw <= 1 ? Math.round(confidenceRaw * 100) + "%" : confidenceRaw + "%";
    } else confidence = String(confidenceRaw);
  }

  return (
    <div className="card judge-card">
      <div className="judge-header">
        <h3>{name}</h3>
        <div className="judge-score">{score}%</div>
      </div>

      <div className="judge-meta">
        <span><strong>Status:</strong> {status}</span>
        <span><strong>Risk:</strong> {risk}</span>
        <span><strong>Confidence:</strong> {confidence}</span>
      </div>

      {judge?.explanation ? <p className="explanation">{judge.explanation}</p> : null}

      {(judge?.strengths || judge?.weaknesses) ? (
        <div className="judge-summary">
          {judge.strengths?.length ? <p><strong>Strengths:</strong> {judge.strengths.join(', ')}</p> : null}
          {judge.weaknesses?.length ? <p><strong>Weaknesses:</strong> {judge.weaknesses.join(', ')}</p> : null}
        </div>
      ) : null}

      <p><strong>Recommendation:</strong> {judge?.recommendation || "None"}</p>

      {judge?.evidence ? (
        <div className="evidence">
          <strong>Evidence:</strong>
          {Array.isArray(judge.evidence) ? (
            <ul>
              {judge.evidence.map((e, i) => (
                <li key={i}>{e}</li>
              ))}
            </ul>
          ) : (
            <ul>
              {Object.entries(judge.evidence).map(([key, value]) => (
                <li key={key}>{`${key}: ${value}`}</li>
              ))}
            </ul>
          )}
        </div>
      ) : null}
    </div>
  );
}
