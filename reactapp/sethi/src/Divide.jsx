import React from "react";

function Divide(a,b)
{
    var c=""+a/b;
    var d="";
    var count=0;
    var flag=0;
    for (var i=0;(i<c.length) && (count<4);++i)
    {
        if(c[i]==".")
        {   flag=1;
            d=d+c[i];
            
        }
        else if(flag==1)
        {
            d=d+c[i];
            count=count+1;
        }
        else{
                d=d+c[i];
        }
    }
return(<h1>Division is {d} </h1>)

}
export default Divide;