import {useState} from "react";

import Navbar from "./components/Navbar";

import EvaluationForm from "./components/EvaluationForm";

import Dashboard from "./components/Dashboard";

import "./styles.css";


function App(){


const [result,setResult]=useState(null);



return(

<div>


<Navbar/>


<div className="container">


<h1 className="title">

AI Response Evaluation Platform

</h1>


<p className="subtitle">

Analyze AI responses using multiple quality judges

</p>



<EvaluationForm

setResult={setResult}

/>



{
result &&

<Dashboard

data={result}

/>

}



</div>


</div>

)

}


export default App;