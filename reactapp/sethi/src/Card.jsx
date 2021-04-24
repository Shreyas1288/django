import React from "react";
import "./index.css";

function Card(prop)
{
return(  <>
    
   
<div className="card">

<img src={prop.imgsrc} alt="my Pic" className="card_img"/>
<div className="card_info">
<br/>
<span className="card_category">{prop.msg}
<br/>
</span>
<h3 className="card_title">{prop.msg1}<br/>
</h3>
<button>{prop.msg2} </button>
</div>

</div>
   
    

        </>);


}
export default Card;