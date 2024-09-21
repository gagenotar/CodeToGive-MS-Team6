import React, { useState, useEffect } from 'react';
import api from '../api';
import AdminNavBar from '../components/AdminNavBar';

const Admin = () => {
    const [admin, setAdmin] = useState({});
    const [jobs, setJobs] = useState([]);
    const jobadmin_id = localStorage.getItem('jobadmin_id');

    useEffect(() => {
        const getAdmin = async () => {
            const response = await api.get(`/job_admin/${jobadmin_id}`);
            setAdmin(response.data);
        };

        const getJobs = async () => {
            const response = await api.get('/job_admin/postedby/' + jobadmin_id);
            setJobs(response.data);
        }

        if (jobadmin_id) {
            getAdmin();
            getJobs();
        }
    }, [jobadmin_id]);

    const displayJobs = () => {
        return jobs.map((job) => {
            return (
                <div className="card mt-3" key={job.id}>
                    <div className="card-body">
                        <h5 className="card-title">{job.title}</h5>
                        <p className="card-text">{job.description}</p>
                        <div className='row mb-3'>
                            <div>
                                <a href="#" className="btn btn-primary mx-1">Edit</a>
                                <a href="#" className="btn btn-danger mx-1">Delete</a>
                            </div>
                        </div>
                        <div className='row'>
                            <div>
                                <a href={`matches/${job.id}`} className="btn btn-primary mx-1">View Matches</a>
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
            <h1>Home</h1>
            <p>Welcome to the admin page, {admin.name}</p>
            <div className="container" id='home-wrapper'>
                <div className="row mb-3 justify-content-center">
                    <div className="col">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Jobs</h5>
                                <p className="card-text">Here are your jobs</p>
                                <a href="/jobs" className="btn btn-primary">Upload Job</a>
                                {displayJobs()}
                                <div className="card mt-3">
                                    <div className="card-body">
                                        <h5 className="card-title">Job Title</h5>
                                        <p className="card-text">Job Description</p>
                                        <div className='row mb-3'>
                                            <div>
                                                <a href="#" className="btn btn-primary mx-1">Edit</a>
                                                <a href="#" className="btn btn-danger mx-1">Delete</a>
                                            </div>
                                        </div>
                                        <div className='row'>
                                            <div>
                                                <a href="#" className="btn btn-primary mx-1">View Matches</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div className="card mt-3">
                                    <div className="card-body">
                                        <h5 className="card-title">Job Title</h5>
                                        <p className="card-text">Job Description</p>
                                        <div className='row mb-3'>
                                            <div>
                                                <a href="#" className="btn btn-primary mx-1">Edit</a>
                                                <a href="#" className="btn btn-danger mx-1">Delete</a>
                                            </div>
                                        </div>
                                        <div className='row'>
                                            <div>
                                                <a href="#" className="btn btn-primary mx-1">View Matches</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="col">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Events</h5>
                                <p className="card-text">Here are your events</p>
                                <a href="/events" className="btn btn-primary">Upload Event</a>
                                {displayJobs()}
                                <div className="card mt-3">
                                    <div className="card-body">
                                        <h5 className="card-title">Event Title</h5>
                                        <p className="card-text">Event Description</p>
                                        <div className='row mb-3'>
                                            <div>
                                                <a href="#" className="btn btn-primary mx-1">Edit</a>
                                                <a href="#" className="btn btn-danger mx-1">Delete</a>
                                            </div>
                                        </div>
                                        <div className='row'>
                                            <div>
                                                <a href="#" className="btn btn-primary mx-1">View Matches</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div className="card mt-3">
                                    <div className="card-body">
                                        <h5 className="card-title">Event Title</h5>
                                        <p className="card-text">Event Description</p>
                                        <div className='row mb-3'>
                                            <div>
                                                <a href="#" className="btn btn-primary mx-1">Edit</a>
                                                <a href="#" className="btn btn-danger mx-1">Delete</a>
                                            </div>
                                        </div>
                                        <div className='row'>
                                            <div>
                                                <a href="#" className="btn btn-primary mx-1">View Matches</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
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
