import React from 'react';

const NavBar = () => {
    return (
        <nav>
            <ul>
                <li><a href="/home">Home</a></li>
                <li><a href="/profile">Profile</a></li>
                <li><a href="/login">Login</a></li>
                <li><a href="/register">Register</a></li>
                <li><a href="/logout">Logout</a></li>
            </ul>
        </nav>
    );
};

export default NavBar;