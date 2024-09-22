import React, { useState, useEffect } from 'react';
import api from '../api';
import AdminNavBar from '../components/AdminNavBar';
import '../styles/Admin.css';

const Admin = () => {
    const [admin, setAdmin] = useState({});
    const [jobs, setJobs] = useState([]);
    const [events, setEvents] = useState([]);
    const jobadmin_id = localStorage.getItem('jobadmin_id');

    useEffect(() => {
        const getAdmin = async () => {
            const response = await api.get(`/job_admin/${jobadmin_id}`);
            setAdmin(response.data);
        };

        const getContent = async () => {
            var response = await api.get('/job_admin/postedby/' + jobadmin_id);
            setJobs(response.data);
            
            response = await api.get('/events/');
            setEvents(response.data);
        }

        if (jobadmin_id) {
            getAdmin();
            getContent();
        }
    }, [jobadmin_id]);

    const truncateText = (text, maxLength) => {
        if (text.length <= maxLength) return text;
        return text.substring(0, maxLength) + '...';
    };

    const displayJobs = () => {
        return jobs.map((job) => {
            return (
                <div className="card mt-3" key={job.job_id}>
                    <div className="card-body">
                        <h5 className="card-title">{job.title}</h5>
                        <p className="card-text">{truncateText(job.description, 150)}</p>
                        <div className='row mb-3'>
                            <div>
                                <a href="#" className="btn btn-primary mx-1">Edit</a>
                                <a href="#" className="btn btn-danger mx-1">Delete</a>
                            </div>
                        </div>
                        <div className='row'>
                            <div>
                                <a href={`matches/${job.job_id}`} className="btn btn-primary mx-1">View Matches</a>
                            </div>
                        </div>
                    </div>
                </div>
            );
        });
    }

    const displayEvents = () => {
        return events.map((event) => {
            return (
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
                                <a href={`participants/${event.event_id}`} className="btn disabled btn-primary mx-1">View Participants</a>
                            </div>
                        </div>
                    </div>
                </div>
            );
        });
    }

    return (
      <div>
        <AdminNavBar />
        <div className='container-fluid'>
            <div className='container-fluid'>
                <h1>Home</h1>
                <p>Welcome to the admin page, {admin.name}</p>
            </div>
            <div className="container" id='home-wrapper'>
                <div className="row mb-3 justify-content-center">
                    <div className="col">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Jobs</h5>
                                <p className="card-text">Here are your jobs</p>
                                <a href="/jobs" className="btn btn-primary">Upload Job</a>
                                {displayJobs()}
                            </div>
                        </div>
                    </div>
                    <div className="col">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Events</h5>
                                <p className="card-text">Here are your events</p>
                                <a href="/events" className="btn btn-primary">Upload Event</a>
                                {displayEvents()}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>
    )
}

export default Admin;
