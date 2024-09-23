import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import NavBar from '../components/NavBar';
import api from '../api';

const Details = () => {
    const { id } = useParams();
    const [jobDetails, setJobDetails] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchDetails = async () => {
            try {
                const jobResponse = await api.get(`/jobs/${id}`);
                console.log(jobResponse.data);
                setJobDetails(jobResponse.data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchDetails();
    }, [id]);

    if (loading) {
        return (
            <div className='container-fluid d-flex justify-content-center align-items-center' style={{ height: '100vh' }}>
                <h1>Loading job details...</h1>
            </div>
        );
    }
    if (error) return <div>Error: {error}</div>;

    const notifySponsor = async () => {
        try {
            // const response = await api.post('/job_admin/notify_student', { student_id, job_id: id });
            const response = { status: 200 };
            console.log(response.data);
            if (response.status === 200) {
                alert('Notification sent successfully!');
            } else {            
                alert('Failed to send notification.');
            }
        } catch (err) {
            console.error(err);
            alert('Failed to send notification.');
        }
    };

    return (
        <div>
            <NavBar />
            <div className='container-fluid'>
                <h1 className="mt-4">Job Details</h1>
                {jobDetails && (
                    <div className="card mb-4">
                        <div className="card-body">
                            <div className='row'>
                                <div className='col'>
                                    <h2>{jobDetails.title}</h2>
                                </div>
                                <div className='col align-items-center'>
                                    <a href="#" onClick={() => notifySponsor()} className="btn btn-primary" style={{ width: '100%' }}>Contact</a>                                        
                                </div>
                            </div>
                            <p className="card-text">{jobDetails.description}</p>
                            <p className="card-text"><strong>Skills Required:</strong> {jobDetails.skills_required}</p>
                            <p className="card-text"><strong>Location:</strong> {jobDetails.street}, {jobDetails.state}, {jobDetails.country}, {jobDetails.zipcode}</p>
                            <p className="card-text"><strong>Posted By:</strong> {jobDetails.posted_by}</p>
                            <p className="card-text"><strong>Application Deadline:</strong> {jobDetails.application_deadline}</p>
                        </div>
                    </div>
                )}                
            </div>
        </div>
    );
};

export default Details;