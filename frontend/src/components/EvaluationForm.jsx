import { useState } from "react";
import { evaluateResponse } from "../services/api";

export default function EvaluationForm({ setResult }) {
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState("");
	const [form, setForm] = useState({ prompt: "", response: "", reference: "" });

	const update = (e) => setForm({ ...form, [e.target.name]: e.target.value });

	const submit = async () => {
		try {
			setLoading(true);
			setError("");

			const data = {
				prompt: form.prompt,
				response: form.response,
				reference: form.reference || form.response,
			};

			const result = await evaluateResponse(data);
			console.log(result);
			setResult(result);
		} catch (err) {
			console.error(err);
			setError("Backend connection failed. Check Django server.");
		} finally {
			setLoading(false);
		}
	};

	return (
		<div className="card">
			<h2>Evaluate Response</h2>

			<textarea name="prompt" placeholder="Enter user prompt" value={form.prompt} onChange={update} />

			<textarea name="response" placeholder="Enter AI generated response" value={form.response} onChange={update} />

			<textarea name="reference" placeholder="Reference answer (optional)" value={form.reference} onChange={update} />

			<button onClick={submit} disabled={loading || !form.prompt.trim() || !form.response.trim()} aria-busy={loading}>
				{loading ? "Evaluating..." : "Evaluate AI Response"}
			</button>

			{error && <p className="error">{error}</p>}
		</div>
	);
}