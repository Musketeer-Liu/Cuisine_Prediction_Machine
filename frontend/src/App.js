import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Home } from './Home';
import  Prediction  from './Prediction';
import { NoMatch } from './NoMatch';
import { Layout } from './components/Layout';
import { NavigationBar } from './components/NavigationBar';
import { Jumbotron } from './components/Jumbotron';
import  Results from './Results';

class App extends Component {
  /*
  The App component is the main file. It is rendering the whole application 
  with different routes  
  */
 handleAddItem = item => {
  this.setState(prevState => ({ items: [...prevState.items, item] }));
};

  render() {
    return (
      <React.Fragment>
        <Router>
          <NavigationBar />
          <Jumbotron />
          <Layout>
            <Switch>
            
            {/*We will replace the App component with a React class,
               which will return a Router component. 
               Router will wrap all of the routes we are going to define. */}
            
              <Route exact path="/" component={Home}  />
              <Route path="/prediction" component={Prediction} />
              <Route path="/results" component={Results} />

              <Route component={NoMatch} />
            </Switch>
          </Layout>
        </Router>
      </React.Fragment>
    );
  }
}

export default App;
