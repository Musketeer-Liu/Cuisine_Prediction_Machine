import React from 'react';
import { Jumbotron as Jumbo, Container } from 'react-bootstrap';
import '../css/components.css';


export const Jumbotron = () => (
/*
  In this component, the jumbotron is showing image
  with the text on it

  */
    <Jumbo fluid className="jumbo">
      <div className="overlay"></div>
      <Container align='center'>
        <h2 className="h2-class">Welcome to the Cuisine Prediction Machine!</h2>
      </Container>
    </Jumbo>

)
