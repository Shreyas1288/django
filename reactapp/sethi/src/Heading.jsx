import React from "react";

import "./index.css";
import { render } from "@testing-library/react";
var css={
    
    
}
var date=new Date().getHours();
var value=""
if((date)==0)
{
value="Good Night Sir";
css.color="green";
}
else if(date<12)
{
value="Good morning sir";
css.color="orange";
}
else if(date>18)
{
value="Good Night sir";
css.color="blue";
}

else
{
value="Good evening sir";
css.color="pink";

}

function Heading(){

    return(<><div className="somu1">
    <div className="somu2">
    <h1 className="somu3">Today time is very very large 
    <span style={css}>  {value}</span>
    </h1>
</div>
</div>
</>);
}

export default Heading;