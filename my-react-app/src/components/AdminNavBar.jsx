import React from 'react';

const AdminNavBar = () => {
    const role = localStorage.getItem('role');

    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav">
                    <li className="nav-item">
                        <a className="nav-link" href='/admin'>Home</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="/jobs">Upload Jobs</a>
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