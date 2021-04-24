import React, { createContext } from "react";
import ComB from "./ComB";

const Fname=createContext();
const Lname=createContext();
var somu="Somu";
const ComA=()=>{

return(<>
<Fname.Provider value={somu}>
<Lname.Provider value={"singh"}>
<ComB/>
</Lname.Provider>
</Fname.Provider>

</>
);

};
export default ComA;
export { Fname,Lname };