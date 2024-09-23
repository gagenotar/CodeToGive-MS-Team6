import React from 'react';
import '../styles/LandingPage.css';
import { ReactTyped } from "react-typed";

const LandingPage = () => {
    return (
        <div className="landing-page">
            <nav className="navbar navbar-expand-lg custom-navbar">
                <a className="navbar-brand" href="/">
                    <img src="/src/img/alpfaLogo.png" alt="Logo" className="navbar-logo" />
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
                    <h1>Welcome to ALPFA Connect</h1>
                    <p>Connecting Latino Leaders for Impact</p>
                    <h4>
                    <ReactTyped
                    strings={[
                        "Hola",
                        "Get connected",
                        "Conéctate",
                        "Find your job",
                        "Encuentra tu trabajo",
                        "Discover events",
                        "Descubre eventos"
                    ]}
                    typeSpeed={120}
                    backSpeed={50}
                    loop
                    />
                </h4>
            </header>
            <section className="mission">
                <div className="container">
                    <h2>Our Mission</h2>
                    <p>At ALPFA Connect, we aim to connect Latino leaders for impact by providing personalized connections to jobs and events. Our platform is designed to enhance satisfaction and streamline the hiring process for both job seekers and sponsors.</p>
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
            </footer>
        </div>
    );
};

export default LandingPage;