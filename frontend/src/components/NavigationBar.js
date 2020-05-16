import React from 'react';
import { Link } from 'react-router-dom';
import { Nav, Navbar } from 'react-bootstrap';
import '../css/components.css';


export const NavigationBar = () => (
  /*
  In this component, the navigation bar is showing with the 
  navigation functionality with the help of Link tag 
  
  */
    <Navbar expand="lg">
      <Navbar.Brand href="/"></Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Item className= 'nav-item-css'>
              <Link className= 'link-css' to="/">Home</Link>
            </Nav.Item>
          <Nav.Item className= 'nav-item-css'>
              <Link className= 'link-css' to="/prediction">Prediction</Link>
         </Nav.Item>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
)
