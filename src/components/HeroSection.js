import React from "react";
import { Button } from "./Button";
import './HeroSection.css';
import '../App.css';

function HeroSection() {
    return (
        <div className='hero-container'>
            <h1>ADVENTURE AWAITS</h1>
            <p>What are you waiting for?</p>
            <div className="hero-btns">
                <Button className='btns' buttonStyle='butn--outline' buttonSize='btn-large'>GET STARTED</Button>
                <Button className='btns' buttonStyle='butn--primary' buttonSize='btn-large'>WATCH TRAILER <i className='far fa-play-cirlce' /></Button>
            </div>
        </div>
    )
}

export default HeroSection