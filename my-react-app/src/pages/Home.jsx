import React, { useState, useEffect } from 'react';
import api from '../api';
import NavBar from '../components/NavBar';
import '../styles/Home.css';

const Home = () => {
    const [student, setStudent] = useState({});
    const [jobs, setJobs] = useState([]);
    const [events, setEvents] = useState([]);
    const [loading, setLoading] = useState(true);
    const student_id = localStorage.getItem('student_id');

    const fetchJobs = async () => {
        try {
            const response = await api.get('/match_job/' + student_id);
            setJobs(response.data);
        } catch (err) {
            console.error(err);
        }
    };

    useEffect(() => {
        const getStudent = async () => {
            const response = await api.get(`/students/${student_id}`);
            setStudent(response.data);
        };

        const getContent = async () => {
            const response = await api.get('/events/');
            setEvents(response.data);
            setLoading(false);
        };

        if (student_id) {
            getStudent();
            getContent();
            fetchJobs();
        }
    }, [student_id]);

    const truncateText = (text, maxLength) => {
        if (text.length <= maxLength) return text;
        return text.substring(0, maxLength) + '...';
    };

    const displayJobs = () => {
        return jobs.map((job) => (
            <div className="card mt-3" key={job.job_id}>
                <div className="card-body">
                    <h5 className="card-title">{job.job_title}</h5>
                    <p>Match score: {job.match_score}</p>
                    <p>Application deadline: {job.application_deadline}</p>
                    <div className='row'>
                        <div>
                            <a href={`details/${job.job_id}`} className="btn btn-primary mx-1">View Job Details</a>
                        </div>
                    </div>
                </div>
            </div>
        ));
    };

    const displayEvents = () => {
        return events.map((event) => (
            <div className="card mt-3" key={event.event_id}>
                <div className="card-body">
                    <h5 className="card-title">{event.event_name}</h5>
                    <p className="card-text">{truncateText(event.event_type, 50)}</p>
                    <p className="card-text">{truncateText(event.description, 150)}</p>
                    <div className='row mb-3'>
                        <div>
                            <a href="#" className="btn btn-primary mx-1">Edit</a>
                            <a href="#" className="btn btn-danger mx-1">Delete</a>
                        </div>
                    </div>
                    <div className='row'>
                        <div>
                            <a href={`participants/${event.event_id}`} className="btn btn-primary mx-1">View Participants</a>
                        </div>
                    </div>
                </div>
            </div>
        ));
    };

    return (
        <div>
            <NavBar />
            <div className='container-fluid'>
                <h1>Home</h1>
                <p>Welcome to the home page, {student.student_name}</p>
            </div>
            <div className="container" id='home-wrapper'>
                <div className="row mb-3">
                    <div className="col">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Profile</h5>
                                {student && (
                                    <div>
                                        <p>{student.student_name}</p>
                                        <p>{student.email}</p>
                                        <p>Experience Level: {student.experience}</p>
                                        <p>{student.major}</p>
                                        <p>{student.university}</p>
                                    </div>
                                )}
                                <a href="/profile" className="btn btn-primary">View Profile</a>
                            </div>
                        </div>
                    </div>
                    <div className="col">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Matched Jobs</h5>
                                <p className="card-text">List of matched jobs</p>
                                <button className="btn btn-primary" onClick={fetchJobs}>Refresh</button>
                                {displayJobs()}
                            </div>
                        </div>
                    </div>
                    <div className="col">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Events</h5>
                                <p className="card-text">List of events</p>
                                {displayEvents()}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Home;