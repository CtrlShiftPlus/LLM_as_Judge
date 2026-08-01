from pprint import pprint

from models_ai.master_llm_judge import MasterJudge

judge = MasterJudge()

local = [

{

"judge":"Toxicity",

"score":100,

"status":"PASS"

},

{

"judge":"Readability",

"score":90,

"status":"PASS"

},

{

"judge":"Completeness",

"score":85,

"status":"WARNING"

}

]

result = judge.evaluate(

"Explain AI",

"Artificial Intelligence is...",

local

)

pprint(result)