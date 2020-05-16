import React from 'react'
import './index.css';
import {  Button } from 'react-bootstrap';



class Results extends React.Component {
   
    onClickHandler=() =>{
        localStorage.clear();
        this.props.history.push('/prediction');
        }
render(){


/*
In this component the demo samples are shown of the how this is works 
*/

    return(
        
  <div >


  

<div className= "predict-align">
        
        <h5>Predictions :</h5>
<br />
        {  
            this.props.location.param1 ?
              
              
               <h4 className='predict-tags'>Cuisine :  &nbsp; &nbsp; &nbsp; &nbsp;<span>   {this.props.location.param1}</span></h4>
              
               :null 
       }
        
        {  
             this.props.location.param2 ?
              
              
               <h4 className='predict-tags'>id : &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp;&nbsp;<span>{this.props.location.param2}</span></h4>
              
               :null 
        }

       {  
             this.props.location.param3 ?
              
              
               <h4 className='predict-tags'>Ingredients : &nbsp;<span>     
               
               
               {this.props.location.param3.map(suggest => <span key={suggest} >{suggest},
               
           
 
                </span>)}
                </span>
              
               </h4>
              
               :null 
       }

               {  
                 this.props.location.param4 ?
              
              
               <h4 className='predict-tags'>Probability : &nbsp;<span> {this.props.location.param4}</span></h4>
              
               :null 
               }

               <Button className="btn-predict" variant="info" size="lg" onClick={this.onClickHandler} type='submit' block>Back to Prediction</Button>{' '}


               </div>
  <br />
  <br />
  
  </div>

    )}
}


export default Results;