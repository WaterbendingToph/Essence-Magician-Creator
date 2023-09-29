import React from 'react';
import '../../App.css';
import './pages.css';
import './EssenceExperimenter.css';
import { Button } from '../Button';
import '../Button.css';
import EssenceSquare from '../EssenceSquare';

function EssenceExperimenter () {
    return (
        <div id='overall-container'>
            {/* <h1>ESSENCE EXPERIMENTER PAGE</h1> */}
            <div className='row-1'>
                <div className='base-essence-container'>
                    <EssenceSquare type='base' name='magic' /> 
                    {/* <h2 id='essence-name-1'>Essence Name 1</h2> */}
                </div>
                
                <div className='base-essence-container'>
                   <EssenceSquare type='base' name='might' /> 
                    {/* <h2 id='essence-name-2'>Essence Name 2</h2> */}
                </div>
                
                <div className='base-essence-container'>
                    <EssenceSquare type='base' name='wing' /> 
                    {/* <h2 id='essence-name-3'>Essence Name 3</h2> */}
                </div>
            </div>

            <div className='row-2'>
                <div className='button-container' id='button-container-1'>
                    <Button target={'/WorldDetails'}>Essence 1 Details</Button>
                    <Button target={'/WorldDetails'}>Essence 2 Details</Button>
                    <Button target={'/WorldDetails'}>Essence 3 Details</Button>
                </div>
                
                <div id='confluence-essence-container' >
                    <EssenceSquare type='confluence' name='dragon' /> 
                    {/* <h2 id='confluence-essence-name'>Confluence Essence Name</h2>  */}
                </div>

                <div className='button-container' id='button-container-2'>
                    <Button target={'/WorldDetails'}>Randomize</Button> 
                    <Button target={'/WorldDetails'}>Confluence Essence Details</Button>
                    <Button target={'/WorldDetails'}>New Confluence Combination</Button>
                </div>
            </div>
        </div>
    )
}

export default EssenceExperimenter;