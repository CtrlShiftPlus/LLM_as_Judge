from .consensus import final_consensus
from .explainability import generate_explanation

# Import your existing judges
# Change names only if your function names are different

from models_ai.toxicity import toxicity_check
from models_ai.hallucination import hallucination_check
from models_ai.completeness import completeness_check
from models_ai.readability import readability_check
from models_ai.similarity import similarity_check



def run_llm_judge(prompt, response):

    results = {}


    # Toxicity
    try:
        results["toxicity"] = toxicity_check(response)

    except Exception as e:
        results["toxicity"] = {
            "error": str(e)
        }



    # Hallucination
    try:
        results["hallucination"] = hallucination_check(
            prompt,
            response
        )

    except Exception as e:
        results["hallucination"] = {
            "error": str(e)
        }



    # Completeness
    try:
        results["completeness"] = completeness_check(
            prompt,
            response
        )

    except Exception as e:
        results["completeness"] = {
            "error": str(e)
        }



    # Readability
    try:
        results["readability"] = readability_check(
            response
        )

    except Exception as e:
        results["readability"] = {
            "error": str(e)
        }



    # Similarity
    try:
        results["similarity"] = similarity_check(
            prompt,
            response
        )

    except Exception as e:
        results["similarity"] = {
            "error": str(e)
        }



    # Final consensus
    final = final_consensus(results)


    # Add explanation layer
    explanation = generate_explanation(
        results,
        final
    )


    return {
        "individual_scores": results,
        "final_consensus": final,
        "explanation": explanation
    }