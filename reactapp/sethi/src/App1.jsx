//To DO list
import React, { useState } from "react"; 
import Todo from "./Todo";
import "./index.css";
import AddIcon from '@material-ui/icons/Add';

const App1=()=>{
const[items,additems]=useState("");
const[Arr,Arr1]=useState([]);
const Func1=(event)=>{
additems(event.target.value);
};

const Func=()=>{
Arr1((prevValue)=>{
return([...prevValue,items]);
})
// Arr1([...prevValue,items]);

additems("");

};


const Func2=(id)=>{
  var flag=0;
  Arr1=[];

  
for (var i=0,j=0;i<Arr.length;++i)
{
 if(i===id)
 {
   flag=1;
 }
 else 
 {
   Arr1[j]=Arr[i];
   j=j+1;
   
 }
 
}

};
return(<>

<div className="somu3">
<div className="border">

<div className="somu4">
<div className="heading">
<h1>To Do list</h1>
</div>
<div className="somu7">
<input className="somu6" type="text" name="field" placeholder="Add a Item" onChange={Func1} value={items} />

<button className="somu8" onClick={Func}>

<AddIcon />


</button>

</div>
<ol>
<div className="somu1">
{Arr.map((value,index)=>{
return(<>
<div className="somu5">
<Todo value1={value} key={index} id={index}  />
</div>
</>
);
})

}
</div>

</ol>
</div>
</div>
</div>
</>

);

};


export default App1;

//To do list
