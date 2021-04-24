import React, { useContext } from "react";
import { Fname,Lname } from "./ComA";


const ComC=()=>{
    const fname1=useContext(Fname);
    const lname1=useContext(Lname);

return(<>
<h1>Hello {fname1} {lname1}</h1>
</>
);

};
export default ComC;