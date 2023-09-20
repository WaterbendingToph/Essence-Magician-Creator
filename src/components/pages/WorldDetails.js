import React from 'react';
import '../../App.css';
import './pages.css';
import Cards from '../Cards';

function WorldDetails () {
    return (
        <div className='worldDetails-container'>
            <h1>WORLD DETAILS PAGE</h1>
            <Cards pages='WorldDetails'/>
        </div>
    )
}

export default WorldDetails;