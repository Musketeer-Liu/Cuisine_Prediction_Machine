import React from 'react';
import axios from 'axios';
import {INGREDIENTS} from './Ingredients';
import { Row,Col, Form , Button ,Container} from 'react-bootstrap';
import ReactTags from 'react-tag-autocomplete'
import './index.css';



// the suggestions having all the ingredients
const suggestions = INGREDIENTS.map((Ingredient) => {
  return {
      name: Ingredient
  }
})


const KeyCodes = {
  comma: 188,
  enter: 13,
};

const delimiters = [KeyCodes.comma, KeyCodes.enter];

// This is use to shuffle the array to avoid getting same suggestions
// all the time
function shuffleArray(array) {
  let i = array.length - 1;
  for (; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    const temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
  return array;
}



class Prediction extends React.Component {
  constructor (props) {
    super(props)
//the following (this.state) take the initial state as empty but every time the state
// change, we will setState as new state of the variable
    this.state = {
      id : '',
      tags: [],
      posts : [],
      suggestions: suggestions,
      suggestions_list: suggestions,
      errorMsg: '',
      data : '',

    }

    //we have to bind all the function in React
    this.handleDelete = this.handleDelete.bind(this);
    this.handleAddition = this.handleAddition.bind(this);


  }

  /*
  This function will delete the tag if user want to remove it
  from ingredients.
 */
componentDidMount(){
  this.setState({
    suggestions_list: shuffleArray(suggestions),
  });

}
  handleDelete(i) {
    const { tags } = this.state;

    // This will filter the index of tag the users
    // want to remove as an tag and set the state which is not same as the tags
    // available in tags
    this.setState({
      tags: tags.filter((tag, index) => index !== i),
    });
  }


  /*
  This function will Add the tag if user want to Add it
  in ingredients.
 */
  handleAddition(tag) {
    const {suggestions} =this.state;

  // This will take all the tags available in tags and
  // add new tag (you can think as an append ,if you are familiar with python)
   this.setState(state => ({ tags: [...state.tags, tag] }));
   this.setState({
    suggestions: shuffleArray(suggestions),

   })

  }

  /*
  This function will send data into api
 */
 submitHandler = e =>{
     e.preventDefault()
    // A new variable is created to get the data
   const newvr=  this.state.tags.map(data => {
      return `${data.name},`;
    })
  // after saving the data, join it by space to convert it into string
    var ing = newvr.join('');
    console.log(ing)


    var ingredients= ing.slice(0, -1);
    console.log(ingredients)
    // ingredients = ingredients.split(' ').join('+')




    //React Http post request is made
     axios.post('http://localhost:5000/prediction?id=' + this.state.id + '&recipes=' + ingredients, {
        })

    //get the response of request
    .then((response) => {
      this.setState({ data: response.data});

      const newTo = {
        pathname: "/results",
        param2: this.state.data.results[0].id,
        param3: this.state.data.results[0].ingredients,
        param1: this.state.data.results[0].cuisine,
        param4: this.state.data.results[0].probability,
      };
      this.props.history.push(newTo);


    }, (error) => {
      console.log('--------------')
      console.log(error);
    });
    }


    // this function is make sure that id is not an alphabets
    onChange = (e)=>{
      const re = /^[0-9\b]+$/;
      if (e.target.value === '' || re.test(e.target.value)) {
        this.setState({id : e.target.value})
      }
    }



// now it`s time to render
render () {

    return (
      <div>
           <div>
           <Form onSubmit ={this.submitHandler}>
<Form.Group controlId="formGroupEmail">
  <Row className="justify-content-md-center">
  <Col md= {7}>
    <Form.Label>ID :</Form.Label>
    <Form.Control type="text" name="id" required="required" value= {this.state.id} placeholder="ID"  onChange={this.onChange} />
  </Col>
  </Row>
</Form.Group>
<Form.Group controlId="formGroupPassword">
<Row className="justify-content-md-center">
  <Col md={{ span: 7, offset: 3 }}>
  <Form.Label>Ingredients :</Form.Label>
  <ReactTags
      placeholder='Type in your Ingredients ...'
      tags={this.state.tags}
      allowNew ={true}
      suggestions={this.state.suggestions}
      delimiters={delimiters}
      handleDelete={this.handleDelete}
      handleAddition={this.handleAddition}
        />
          <br />

    <Button variant="info" size="lg"  type='submit' block> Predict</Button>{' '}

  </Col>

    </Row>

</Form.Group>
</Form>

             {/* /* this.state.data.map(data => <div key={data.id}>{data.name}</div>): */ }

              {/*Below I am checking either the state.data is empty? if not, print the data
                else just give null
                 */}

   {
               this.state.suggestions_list ?

               <Container className="consug">

               <h5>Some Recipes you may like:</h5>
               <br />

               <Container>
                <div className="row">
               <p>{this.state.suggestions_list.slice(0,50).map(suggest => <span key={suggest.name} className='suggestions-tag'>{suggest.name} </span>)}</p>

               {/* <div className="col-md-4">
               <p>{this.state.suggestions_list.slice(17,33).map(suggest => <div className='suggestions-tag'>{suggest.name} </div>)}</p>
               </div>

               <div className="col-md-4">
               <p>{this.state.suggestions_list.slice(33,50).map(suggest => <div className='suggestions-tag'>{suggest.name} </div>)}</p>
               </div> */}

               </div>
               </Container>

               </Container>

               :null
               }


         </div>
      </div>
    )
  }
}

export default Prediction;
