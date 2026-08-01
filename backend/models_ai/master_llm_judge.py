import os
import json
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

ENABLE_GEMINI = (
    os.getenv("ENABLE_GEMINI","False")
    == "True"
)

if ENABLE_GEMINI:

    genai.configure(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    MODEL_NAME = os.getenv(
        "GEMINI_MODEL",
        "gemini-flash-latest"
    )

    model = genai.GenerativeModel(
        MODEL_NAME
    )


class MasterJudge:

    def evaluate(

        self,

        prompt,

        response,

        local_results

    ):

        if not ENABLE_GEMINI:
            failed = [
                r["judge"]
                for r in local_results
                if r.get("status") != "PASS"
            ]
            passed = [
                r["judge"]
                for r in local_results
                if r.get("status") == "PASS"
            ]
            score = round(
                sum(
                    r.get("score", 0)
                    for r in local_results
                )
                /
                max(len(local_results), 1)
            )
            if any(r.get("status") == "FAIL" for r in local_results):
                status = "FAIL"
                risk = "High"
            elif any(r.get("status") == "WARNING" for r in local_results):
                status = "WARNING"
                risk = "Medium"
            else:
                status = "PASS"
                risk = "Low"

            if failed:
                if failed and not passed:
                    summary = (
                        f"{len(failed)} judge(s) failed: {', '.join(failed)}. "
                        "The response needs targeted improvement in these areas."
                    )
                else:
                    summary = (
                        f"{len(failed)} judge(s) did not pass: {', '.join(failed)}. "
                        f"Focus on those checks while preserving the strengths from {', '.join(passed)}."
                    )
                recommendation = (
                    "Review the failed checks and update the response to better satisfy the prompt, "
                    "reference, and quality expectations. Specifically address: "
                    f"{', '.join(failed)}. "
                    "After revising, re-run evaluation to ensure issues are resolved."
                )
            else:
                summary = (
                    "All local validators passed. The response is strong, "
                    "but enabling Gemini would provide a deeper final review."
                )
                recommendation = "Enable Gemini for a deeper AI review."

            return {
                "judge": "Master Local Judge",
                "score": score,
                "status": status,
                "risk": risk,
                "confidence": 1.0,
                "summary": summary,
                "recommendation": recommendation,
                "strengths": passed,
                "weaknesses": failed,
            }

        prompt_text = f"""
You are an AI Judge.

User Prompt:

{prompt}

AI Response:

{response}

Local Judge Results:

{json.dumps(local_results,indent=2)}

Review the response and the local judge results.

Return ONLY JSON.

{{
"judge":"Master LLM Judge",

"score":95,

"status":"PASS",

"risk":"Low",

"confidence":0.96,

"summary":"",

"recommendation":""

}}

No markdown.

Only JSON.
"""

        reply = model.generate_content(

            prompt_text

        )

        text = reply.text.strip()

        if text.startswith("```"):

            text = text.replace(
                "```json",""
            )

            text = text.replace(
                "```",""
            )

            text = text.strip()

        return json.loads(text)