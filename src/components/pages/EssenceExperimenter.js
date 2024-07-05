import React from 'react';
import '../../App.css';
import './pages.css';
import './EssenceExperimenter.css';
import { Button } from '../Button';
import '../Button.css';
import EssenceSquare from '../EssenceSquare';
import dropdownOptions from '../DropdownOptions';
import '../EssenceSquare.css';

let base1 = <EssenceSquare type='base' name='magic' srcString='/images/essences/'/>;
let base2 = <EssenceSquare type='base' name='might' srcString='/images/essences/'/>;
let base3 = <EssenceSquare type='base' name='wing' srcString='/images/essences/'/>;
let confluence = <EssenceSquare type='confluence' name='dragon' srcString='/images/essences/'/>


export function replaceEssenceSquare(variableName, newEssenceName) {
    if (variableName === 'base1') {
        base1 = <EssenceSquare type ='base' name={newEssenceName} srcString='/images/essences/'/>
    } else if (variableName === 'base2') {
        base2 = <EssenceSquare type ='base' name={newEssenceName} srcString='/images/essences/'/>
    } else if (variableName === 'base3') {
        base3 = <EssenceSquare type ='base' name={newEssenceName} srcString='/images/essences/'/>
    } else if (variableName === 'confluence') {
        confluence = <EssenceSquare type ='confluence' name={newEssenceName} srcString='/images/essences/'/>
    }
}

function EssenceExperimenter () {




    return (
        <div id='overall-container'>
            {/* <h1>ESSENCE EXPERIMENTER PAGE</h1> */}
            <div className='row-1'>
                <div className='base-essence-container'>
                    {base1}
                    {/* <label for='dropdown-label'>Choose a new Essence</label> */}
                    <select name="dropdown-select" id="base1DropdownSelect">
                        {dropdownOptions('base', 'base1')}
                    </select>
                    {/* <EssenceSquare type='base' name='magic' srcString='/images/essences/'/>  */}
                    {/* <h2 id='essence-name-1'>Essence Name 1</h2> */}
                </div>
                
                <div className='base-essence-container'>
                    {base2}
                    {/* <label for='dropdown-label'>Choose a new Essence</label> */}
                    <select name="dropdown-select" id="base2DropdownSelect">
                        {dropdownOptions('base', 'base2')}
                    </select>
                   {/* <EssenceSquare type='base' name='might' srcString='/images/essences/'/>  */}
                    {/* <h2 id='essence-name-2'>Essence Name 2</h2> */}
                </div>
                
                <div className='base-essence-container'>
                    {base3}
                    {/* <label for='dropdown-label'>Choose a new Essence</label> */}
                    <select name="dropdown-select" id="base3DropdownSelect">
                        {dropdownOptions('base')}
                    </select>
                    {/* <EssenceSquare type='base' name='wing' srcString='/images/essences/'/>  */}
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
                    {confluence}
                    {/* <label for='dropdown-label'>Choose a new Essence</label> */}
                    <select name="dropdown-select" id="confluenceDropdownSelect">
                        {dropdownOptions('confluence')}
                    </select>
                    {/* <EssenceSquare type='confluence' name='dragon' srcString='/images/essences/'/>  */}
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