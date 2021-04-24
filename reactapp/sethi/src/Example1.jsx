import React from "react";
import NavBar1 from "./NavBar1";
import { Switch,Route } from "react-router-dom";


const Example1=()=>{

return(<>
<NavBar1/>
    <Switch>
    <Route exact path="/" >
    <h1>This is contact us</h1>
</Route>
<Route path="/about" >
    <h1>This is about us</h1>
</Route>
    </Switch>

    </>
    );

};
export default Example1;