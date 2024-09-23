import React from 'react';
import logo from '../img/alpfaLogo.png';

const NavBar = () => {
    const role = localStorage.getItem('role');

    return (
        <nav className="navbar navbar-expand-lg custom-navbar">
            <a className="navbar-brand" href="/home">
                <img src={logo} alt="Logo" className="navbar-logo" />
            </a>
            <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav">
                    <li className="nav-item">
                        <a className="nav-link" href={role === 'admin' ? '/admin' : '/home'}>Home</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/profile">Profile</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/logout">Logout</a>
                    </li>
                </ul>
            </div>
        </nav>
    );
};

export default NavBar;