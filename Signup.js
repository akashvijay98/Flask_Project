import React, { Component } from 'react';
import GoogleLogin from "react-google-login";
import FacebookLogin from 'react-facebook-login';

import "./Signup.css";

export default class Signup extends React.Component {
  render() {
    return ( 
    <div className="container-fluid">
      <div className="row">
      
      
      
    
      
      <GoogleLogin
    clientId="658977310896-knrl3gka66fldh83dao2rhgbblmd4un9.apps.googleusercontent.com"
    buttonText="Login"
    
    cookiePolicy={'single_host_origin'}
  />
  
  &nbsp; &nbsp;

<FacebookLogin
    appId="1088597931155576"
    autoLoad={true}
    fields="name,email,picture"
     />
     </div>

     
    




             
            </div>

 
     

    
  
      
  
      );
  }
}
