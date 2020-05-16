import React from 'react';
import { Container } from 'react-bootstrap';

export const Layout = (props) => (
/*
Some components don’t know their children ahead of time. 
This is especially common for components like Sidebar or Dialog that represent generic “boxes”.

We recommend that such components use the special 
children prop to pass children elements directly into their output:
*/

  <Container>
    {props.children}
  </Container>
)
