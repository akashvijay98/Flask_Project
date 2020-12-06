import React, { Component } from 'react';
import Signup from "../component/Signup";
export default class Form extends React.Component {
  render() {
    return( 
    
    <div>
      
    
        
   

          <div className="wrapper">
          <h1>Create Your Account </h1>
          <Signup/>
          <div> <h2>Or</h2> </div>
        <div className="form-wrapper">
          
          <form onSubmit={this.handleSubmit} noValidate>
            <div className="firstName">
              <label htmlFor="firstName">First Name</label>
              <input
              
                placeholder="First Name"
                type="text"
                name="firstName"
                noValidate
                
              />
             
            </div>
            <div className="lastName">
              <label htmlFor="lastName">Last Name</label>
              <input
               
                placeholder="Last Name"
                type="text"
                name="lastName"
                noValidate
                
              />
              
            </div>
            <div className="email">
              <label htmlFor="email">Email</label>
              <input
               
                placeholder="Email"
                type="email"
                name="email"
                noValidate
               
              />
             
            </div>
            <div className="password">
              <label htmlFor="password">Password</label>
              <input
               
                placeholder="Password"
                type="password"
                name="password"
                noValidate
                
              />
            
            </div>
            <div className="createAccount">
              <button type="submit">Create Account</button>
              <small>Already Have an Account?</small>
            </div>
          </form>
        </div>
      </div>
          </div>

          );
  }

}
