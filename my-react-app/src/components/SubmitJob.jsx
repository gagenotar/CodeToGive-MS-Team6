import React, { useState } from 'react';

const SubmitJob = () => {
    const [job, setJob] = useState({
        title: '',
        description: '',
        skills_required: '',
        experience_required: '',
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
        valid_majors: ''
    });

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setJob({
            ...job,
            [name]: type === 'checkbox' ? checked : value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Job submitted:', job);
        // Add your form submission logic here
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Title:</label>
                <input type="text" name="title" value={job.title} onChange={handleChange} required />
            </div>
            <div>
                <label>Description:</label>
                <textarea name="description" value={job.description} onChange={handleChange} required />
            </div>
            <div>
                <label>Skills Required:</label>
                <input type="text" name="skills_required" value={job.skills_required} onChange={handleChange} required />
            </div>
            <div>
                <label>Experience Required (years):</label>
                <input type="number" name="experience_required" value={job.experience_required} onChange={handleChange} required />
            </div>
            <div>
                <label>Street:</label>
                <input type="text" name="street" value={job.street} onChange={handleChange} required />
            </div>
            <div>
                <label>State:</label>
                <input type="text" name="state" value={job.state} onChange={handleChange} required />
            </div>
            <div>
                <label>Country:</label>
                <input type="text" name="country" value={job.country} onChange={handleChange} required />
            </div>
            <div>
                <label>Zipcode:</label>
                <input type="text" name="zipcode" value={job.zipcode} onChange={handleChange} required />
            </div>
            <div>
                <label>Company Name:</label>
                <input type="text" name="company_name" value={job.company_name} onChange={handleChange} required />
            </div>
            <div>
                <label>Salary Range:</label>
                <input type="text" name="salary_range" value={job.salary_range} onChange={handleChange} required />
            </div>
            <div>
                <label>Employment Type:</label>
                <input type="text" name="employment_type" value={job.employment_type} onChange={handleChange} required />
            </div>
            <div>
                <label>Application Deadline:</label>
                <input type="date" name="application_deadline" value={job.application_deadline} onChange={handleChange} required />
            </div>
            <div>
                <label>Bachelor's Degree Needed:</label>
                <input type="checkbox" name="bachelors_needed" checked={job.bachelors_needed} onChange={handleChange} />
            </div>
            <div>
                <label>Master's Degree Needed:</label>
                <input type="checkbox" name="masters_needed" checked={job.masters_needed} onChange={handleChange} />
            </div>
            <div>
                <label>Valid Majors:</label>
                <input type="text" name="valid_majors" value={job.valid_majors} onChange={handleChange} required />
            </div>
            <button type="submit">Submit Job</button>
        </form>
    );
};

export default SubmitJob;