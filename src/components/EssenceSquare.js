import React from "react";
import './EssenceSquare.css';
import dropdownOptions from "./DropdownOptions"; 





function EssenceSquare(props) {
    let srcString = './images/';
    if (props.type == 'base') {
        srcString = './images/essences/base/'.concat(props.name).concat(".png");
    } else if (props.type == 'confluence') {
        srcString = "./images/essences/confluence/".concat(props.name).concat(".png");
    }

    return (
        <>
            <figure className='essenceImage'
                    data-category={props.name.replace(props.name.substr(0, 1), props.name.substr(0, 1).toUpperCase() ) }>
                <img src={srcString} alt={props.name} />
                <label for='dropdown-label'>Choose a new Essence</label>
                    {dropdownOptions(props)}
            </figure>
        </>
    );
}

export default EssenceSquare;