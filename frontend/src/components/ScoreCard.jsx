export default function ScoreCard({score}){


return(

<div className="score">


<h2>
Overall Score
</h2>


<h1>
{score}%
</h1>


<p>

{
score>=85?
"PASS":
score>=70?
"WARNING":
"FAIL"

}

</p>


</div>

)

}