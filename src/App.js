import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Home from './components/pages/Home';
import DMPages from './components/pages/DMPages';
import WorldDetails from './components/pages/WorldDetails';
import Notes from './components/pages/Notes';
import PlayerPages from './components/pages/PlayerPages';
import CombatEncounters from './components/pages/CombatEncounters';
import Shops from './components/pages/Shops';


function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route path='/' exact Component={Home} />
          <Route path='/DMPages' exact Component={DMPages} />
          <Route path='/WorldDetails' exact Component={WorldDetails} />
          <Route path='/Notes' exact Component={Notes} />
          <Route path='/PlayerPages' exact Component={PlayerPages} />
          <Route path='/CombatEncounters' exact Component={CombatEncounters} />
          <Route path='/Shops' exact Component={Shops} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
