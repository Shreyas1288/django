import React from "react";
import { Link } from "react-router-dom";

const NavBar1=()=>{

    return(<>
    <Link to="/">
       <h2>Contact us</h2>
       </Link>
       <Link to="/about">
       <h2>About Us </h2>
       </Link>
        </>
        );
    
    };
    export default NavBar1;