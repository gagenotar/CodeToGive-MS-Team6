import React from 'react';
import Typed from 'react-typed';
import '../styles/LandingPage.css'; // Import the CSS file

const LandingPage = () => {
    return (
        <div className="landing-page">
            <nav className="navbar navbar-expand-lg navbar-light bg-light custom-navbar">
                <a className="navbar-brand" href="/">
                    <img src="/src/img/alpfaLogo.png" alt="Logo" className="navbar-logo" />
                    ALPFA Power
                </a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav ml-auto">
                        <li className="nav-item">
                            <a className="nav-link" href="/login">Login</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="/register">Register</a>
                        </li>
                    </ul>
                </div>
            </nav>
            <header className="header text-center">
                <h1>Welcome to ALPFA Power</h1>
                <p>Connecting Latino Leaders for Impact</p>
                <p>
                    Our platform provides{' '}
                    <Typed
                        strings={[
                            'personalized connections to jobs.',
                            'tailored recommendations for events.',
                            'a streamlined hiring process.',
                        ]}
                        typeSpeed={40}
                        backSpeed={50}
                        loop
                    />
                </p>
            </header>
            <section className="mission">
                <div className="container">
                    <h2>Our Mission</h2>
                    <p>At ALPFA Power, we aim to connect Latino leaders for impact by providing personalized connections to jobs and events. Our platform is designed to enhance satisfaction and streamline the hiring process for both job seekers and sponsors.</p>
                </div>
            </section>
            <section className="goals">
                <div className="container">
                    <h2>Our Goals</h2>
                    <ul>
                        <li>Provide tailored recommendations for members seeking jobs.</li>
                        <li>Help sponsors find the best candidates for their needs.</li>
                        <li>Enhance satisfaction for both job seekers and sponsors.</li>
                        <li>Streamline the hiring process for all parties involved.</li>
                    </ul>
                </div>
            </section>
            <footer className="footer">
                <div className="container text-center">
                    <p>&copy; 2023 ALPFA Power. All rights reserved.</p>
                </div>
            </footer>
        </div>
    );
};

export default LandingPage;