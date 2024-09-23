import React, { useState } from 'react';
import api from '../api';
import AdminNavBar from '../components/AdminNavBar';
import '../styles/jobs.css';

const Jobs = () => {
    const jobadmin_id = parseInt(localStorage.getItem('jobadmin_id'), 10);
    const [job, setJob] = useState({
        job_id: 0,
        title: '',
        description: '',
        skills_required: '',
        experience_required: 0,
        street: '',
        state: '',
        country: '',
        zipcode: '',
        company_name: '',
        salary_range: '',
        employment_type: '',
        application_deadline: '',
        bachelors_needed: false,
        masters_needed: false,
        valid_majors: '',
        posted_by: jobadmin_id,
        posted_at: ''
    });

    const [message, setMessage] = useState('');

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setJob({
            ...job,
            [name]: type === 'checkbox' ? checked : (name === 'experience_required' || name === 'posted_by' ? parseInt(value) : value)
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log(job); // Log the job object to verify its structure
        try {
            const response = await api.post('/jobs', job);
            if (response.status === 200) {
                setMessage('Job posted successfully!');
                // Clear the form
                setJob({
                    job_id: 0,
                    title: '',
                    description: '',
                    skills_required: '',
                    experience_required: 0,
                    street: '',
                    state: '',
                    country: '',
                    zipcode: '',
                    company_name: '',
                    salary_range: '',
                    employment_type: '',
                    application_deadline: '',
                    bachelors_needed: false,
                    masters_needed: false,
                    valid_majors: '',
                    posted_by: jobadmin_id,
                });
            } else {
                setMessage('Failed to post job.');
            }
        } catch (error) {
            setMessage('Failed to post job.');
        }
    };

    return (
        <div>
            <AdminNavBar />
            <div className="jobs-wrapper">
                <div className='m-5 card'>
                    <h1>Create a Job</h1>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label htmlFor="title" className="form-label">Title</label>
                            <input type="text" className="form-control" id="title" name="title" value={job.title} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="description" className="form-label">Description</label>
                            <textarea className="form-control" id="description" name="description" value={job.description} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="skills_required" className="form-label">Skills Required</label>
                            <input type="text" className="form-control" id="skills_required" name="skills_required" value={job.skills_required} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="street" className="form-label">Street</label>
                            <input type="text" className="form-control" id="street" name="street" value={job.street} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="state" className="form-label">State</label>
                            <input type="text" className="form-control" id="state" name="state" value={job.state} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="country" className="form-label">Country</label>
                            <input type="text" className="form-control" id="country" name="country" value={job.country} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="zipcode" className="form-label">Zipcode</label>
                            <input type="text" className="form-control" id="zipcode" name="zipcode" value={job.zipcode} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="company_name" className="form-label">Company Name</label>
                            <input type="text" className="form-control" id="company_name" name="company_name" value={job.company_name} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="salary_range" className="form-label">Salary Range</label>
                            <input type="text" className="form-control" id="salary_range" name="salary_range" value={job.salary_range} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="employment_type" className="form-label">Employment Type</label>
                            <input type="text" className="form-control" id="employment_type" name="employment_type" value={job.employment_type} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="application_deadline" className="form-label">Application Deadline</label>
                            <input type="date" className="form-control" id="application_deadline" name="application_deadline" value={job.application_deadline} onChange={handleChange} required />
                        </div>
                        <div className="form-check mb-3">
                            <input type="checkbox" className="form-check-input" id="bachelors_needed" name="bachelors_needed" checked={job.bachelors_needed} onChange={handleChange} />
                            <label className="form-check-label" htmlFor="bachelors_needed">Bachelors Needed</label>
                        </div>
                        <div className="form-check mb-3">
                            <input type="checkbox" className="form-check-input" id="masters_needed" name="masters_needed" checked={job.masters_needed} onChange={handleChange} />
                            <label className="form-check-label" htmlFor="masters_needed">Masters Needed</label>
                        </div>
                        <div className="mb-3">
                            <label htmlFor="valid_majors" className="form-label">Valid Majors</label>
                            <input type="text" className="form-control" id="valid_majors" name="valid_majors" value={job.valid_majors} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="experience_required" className="form-label">Experience Level Required</label>
                            <input type="number" className="form-control" id="experience_required" name="experience_required" value={job.experience_required} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="posted_at" className="form-label">Posted At</label>
                            <input type="datetime-local" className="form-control" id="posted_at" name="posted_at" value={job.posted_at} onChange={handleChange} required />
                        </div>
                        <button type="submit" className="btn btn-primary">Submit</button>
                    </form>
                    {message && <p className="mt-3">{message}</p>}
                </div>
            </div>
        </div>
    );
};

export default Jobs;