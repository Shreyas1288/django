import React, { useState } from "react";


const App2=()=>{
const[j,newj]=useState(10);
var p=0;

const func=(event)=>{
 if(event.target.name==="button1")   
 {++p;
    newj(j+1);
 }
 else{
if(j===0)
{
    alert("Its zero");
    return;
}
else{
newj(j-1);
}
 }
};

return(
<>
Count {j}
<button onClick={func} name="button1">Increment</button>
<button onClick={func} name="button2">Decrement</button>
{p}
</>
);

};

export default App2;
