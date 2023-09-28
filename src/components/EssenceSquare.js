import React from "react";
import './EssenceSquare.css';

function EssenceSquare(props) {
    if (props.type == 'base') {
        let srcString = "./images/essences/base/".concat(props.name).concat(".png");
        return (
            <>
                <figure className='essenceImage'
                        data-category={props.name.replace(props.name.substr(0, 1), props.name.substr(0, 1).toUpperCase() ) }>
                    <img src={srcString} alt={props.name} />
                </figure>
            </>
        );
    }

    if (props.type == 'confluence') {
        let srcString = "./images/essences/confluence/".concat(props.name).concat(".png");
        return (
            <>
                <figure className='essenceImage'
                        data-category={props.name.replace(props.name.substr(0, 1), props.name.substr(0, 1).toUpperCase() ) }>
                    <img src={srcString} alt={props.name} />
                </figure>
            </>
        )
    }
}

export default EssenceSquare;