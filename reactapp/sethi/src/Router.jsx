import React from "react";
import { BrowserRouter } from "react-router-dom";
import Example1 from "./Example1";
import NavBar1 from "./NavBar1";
const Router=()=>{

    return(
        <>
<BrowserRouter>

<Example1/>
</BrowserRouter>
</>
    );
}; 
export default Router;