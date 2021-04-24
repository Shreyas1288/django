import React, { useState } from "react";
//2 input field

const App3=()=>{
    const[name,setname]=useState({
        lname:"",
        fname:"",
    });
    const Func1=(event)=>{
    var name1=event.target.name;
    var value1=event.target.value;

    setname((prevValue)=>{
        return{...prevValue,
            [name1]:value1,
        }

    });
    
    };
    const Submit=(event)=>{
        event.preventDefault();
    };
return(
<>Hello {name.lname} {name.fname}
<form onSubmit={Submit}>
<input type="text" name="lname" placeholder="Enter name" onChange={Func1}/>
<input type="text" name="fname" placeholder="Enter name" onChange={Func1}/>
<input type="submit" name="Submit" value="Submit" />
</form>
</>
);
};

export default App3;