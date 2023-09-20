import React, { useState, useEffect } from 'react'
import {Link} from 'react-router-dom';
import './Navbar.css'

function Navbar() {
    const [click, setClick] = useState(false)
    const [button, setButton] = useState(true)

    const handleClick = () => setClick(!click);
    const closeMobileMenu = () => setClick(false);

    const showButton = () => {
        if (window.innerWidth <= 960) {
            setButton(false);
        } else {
            setButton(true);
        }
    };

    useEffect(() => {
        showButton()
    }, [] );

    window.addEventListener('resize', showButton);

    return (
        <>
            <nav className="navbar">
                <div className="navbar-container">
                    <Link to="/" className="navbar-logo" onClick={closeMobileMenu}>
                        Home <i className='fab fa-typo3' />
                    </Link>
                    <div className='menu-icon' onClick={handleClick}>
                        <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
                    </div>
                    <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                        <li className='nav=item'>
                            <Link to='/CombatEncounters' className='nav-links' onClick={closeMobileMenu}>Combat Encounters</Link>
                        </li>
                        <li className='nav=item'>
                            <Link to='/DMPages' className='nav-links' onClick={closeMobileMenu}>DM Pages</Link>
                        </li>
                        <li className='nav=item'>
                            <Link to='/Notes' className='nav-links' onClick={closeMobileMenu}>Notes</Link>
                        </li>
                        <li className='nav=item'>
                            <Link to='/PlayerPages' className='nav-links' onClick={closeMobileMenu}>Player's Pages</Link>
                        </li>
                        <li className='nav=item'>
                            <Link to='/Shops' className='nav-links' onClick={closeMobileMenu}>Shops</Link>
                        </li>
                        <li className='nav=item'>
                            <Link to='/WorldDetails' className='nav-links' onClick={closeMobileMenu}>World Details</Link>
                        </li>
                    </ul>
                </div>
            </nav>
        </>
    )
}

export default Navbar