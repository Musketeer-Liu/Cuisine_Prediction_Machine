import React from 'react'
import './App.css';
import Carousel from 'react-bootstrap/Carousel'
import logo from './assets/img1.jpg';
import logo1 from './assets/img2.jpg';
import logo2 from './assets/img3.jpg';
import logo3 from './assets/img4.jpg';
import logo4 from './assets/img5.JPG';
import logo5 from './assets/img6.JPG';

import './css/components.css';

export const Home = () => (
   /*
    In this component the demo samples are shown of the how this is works
  */

  <div >



  <h1 className='mb'>Demo Sample !</h1>

  <Carousel>

  <Carousel.Item>

    <img
      className="d-block w-100 image-dark"
      width='800'
      height='400'
      src={logo}
      alt="First slide"
    />
    <Carousel.Caption>
    <h2 align ='left'>This is the first time Test !</h2>

    <h3 align ='left'>Test 122334 has recipe of :</h3>
      <h4 align ='left'>Yogurt<br />Carrots<br />Sauce Tamoto<br />Salt</h4>

    </Carousel.Caption>
  </Carousel.Item>

  <Carousel.Item>

    <img
      className="d-block w-100 image-dark"
      width='800'
      height='400'
      src={logo4}
      alt="First slide"
    />
    <Carousel.Caption>
    <h2 align ='left'>This is the first time Test !</h2>

    <h3 align ='left'>Test 13245 has recipe of :</h3>

      <h4 align ='left'>White Onion <br />Carrots<br />Chicken<br />Sauce Tamoto</h4>

    </Carousel.Caption>
  </Carousel.Item>

  <Carousel.Item>

    <img
      className="d-block w-100 image-dark"
      width='800'
      height='400'
      src={logo5}
      alt="First slide"
    />
    <Carousel.Caption>
    <h2 align ='left'>This is the first time Test !</h2>

    <h3 align ='left'>Test 444334 has recipe of :</h3>

      <h4 align ='left'>White Onion <br />Spaghetti<br />Carrots<br />Tamoto</h4>

    </Carousel.Caption>
  </Carousel.Item>


  <Carousel.Item>

    <img
      className="d-block w-100 image-dark"
      width='800'
      height='400'
      src={logo3}
      alt="First slide"
    />
    <Carousel.Caption>
    <h2 align ='left'>This is the first time Test !</h2>

    <h3 align ='left'>Test 444334 has recipe of :</h3>

      <h4 align ='left'>White Onion <br />Carrots<br />Sauce Tamoto</h4>

    </Carousel.Caption>
  </Carousel.Item>

  <Carousel.Item>
    <img
      className="d-block w-100"
      width='800'
      height='400'
      src={logo1}
      alt="second slide"
    />

    <Carousel.Caption>
    <h2 align ='left'>This is the first time Test !</h2>

    <h3 align ='left'>Test 423334 has recipe of :</h3>

      <h4 align ='left'>Chicken <br />Cheese <br />Fine Sea Salt<br />Sauce Tamoto</h4>

    </Carousel.Caption>
  </Carousel.Item>
  <Carousel.Item>
    <img
      className="d-block w-100"
      width='800'
      height='400'
      src={logo2}
      alt="Third slide"
    />

    <Carousel.Caption>
    <h2 align ='left'>This is the first time Test !</h2>

    <h4 align ='left'>Test 32322 has recipe of :</h4>

      <h3 align ='left'>Rice<br />Egg<br />Chicken<br />Beef Brisket</h3>
    </Carousel.Caption>
  </Carousel.Item>
</Carousel>

  <br />
  <br />

  </div>
)
