from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from models_ai.completeness import CompletenessJudge
from models_ai.hallucination import HallucinationJudge
from models_ai.readability import ReadabilityJudge
from models_ai.toxicity import ToxicityJudge
from models_ai.similarity import SimilarityJudge
from models_ai.consistency import ConsistencyJudge
from models_ai.consensus import ConsensusJudge
from models_ai.master_llm_judge import MasterJudge


def health_check(request):
    return JsonResponse({
        "status": "running",
        "service": "LLM Judge Backend",
        "version": "1.0"
    })


@csrf_exempt
def evaluate_response(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "POST request required"},
            status=405
        )

    try:

        body = json.loads(request.body)

        prompt = body.get("prompt", "")
        response = body.get("response", "")
        reference = body.get("reference", "")

        # -----------------------
        # Run all judges
        # -----------------------

        completeness = CompletenessJudge().evaluate(
            prompt,
            response
        )

        hallucination = HallucinationJudge().evaluate(
            reference,
            response
        )

        readability = ReadabilityJudge().evaluate(
            response
        )

        toxicity = ToxicityJudge().evaluate(
            response
        )

        similarity = SimilarityJudge().evaluate(
            prompt,
            response
        )

        # build initial judges list (consistency is computed over these)
        judges = [
            completeness,
            hallucination,
            readability,
            toxicity,
            similarity
        ]

        consistency = ConsistencyJudge().evaluate(judges)

        # append consistency result to judges
        judges.append(consistency)

        consensus = ConsensusJudge().evaluate(
            judges
        )

        master = MasterJudge().evaluate(
            prompt,
            response,
            judges
        )

        return JsonResponse({

            "prompt": prompt,

            "response": response,

            "reference": reference,

            "judges": judges,

            "consensus": consensus,

            "master_judge": master

        })

    except Exception as e:

        return JsonResponse(
            {
                "error": str(e)
            },
            status=500
        )