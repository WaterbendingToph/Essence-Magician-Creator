import React from "react";
import CardItem from "./CardItem";
import './Cards.css';

function Cards(props) {
    if (props.pages == 'WorldDetails') {
        return (
                <div className="cards__container">
                    <ul className="cards__wrapper">
                        <CardItem src='./images/img-home.jpg' text="Discover what magic you could have!" label="Essence Experimenter" path="/essenceExperimenter"/>
                        <CardItem src='./images/img-home.jpg' text="Explore all known essence abilities!" label="Still deciding if I want to build this yet, check back later" path="/"/>
                    </ul>
                </div>
        )
    }
}

export default Cards;