import React from 'react';
import logo from '../img/alpfaLogo.png';
import '../styles/AdminNavBar.css';

const AdminNavBar = () => {
    return (
        <nav className="navbar navbar-expand-lg custom-navbar">
            <a className="navbar-brand" href="/admin">
                <img src={logo} alt="Logo" className="navbar-logo" />
            </a>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav">
                    <li className="nav-item">
                        <a className="nav-link" href='/admin'>Home</a>
                    </li>
                    <li className="nav-item dropdown">
                        <a className="nav-link dropdown-toggle" href="#" id="uploadDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Upload
                        </a>
                        <ul className="dropdown-menu" aria-labelledby="uploadDropdown">
                            <li><a className="dropdown-item" href="/jobs">New Job</a></li>
                            <li><a className="dropdown-item" href="/events">New Event</a></li>
                        </ul>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/logout">Logout</a>
                    </li>
                </ul>
            </div>
        </nav>
    );
};

export default AdminNavBar;