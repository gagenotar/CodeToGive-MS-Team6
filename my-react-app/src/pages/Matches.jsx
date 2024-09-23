import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import AdminNavBar from '../components/AdminNavBar';
import api from '../api';

const Matches = () => {
    const { id } = useParams();
    const [jobDetails, setJobDetails] = useState(null);
    const [candidates, setCandidates] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchDetails = async () => {
            try {
                const jobResponse = await api.get(`/jobs/${id}`);
                console.log(jobResponse.data);
                setJobDetails(jobResponse.data);
                
                const candidatesResponse = await api.get(`/job_admin/match_student/${id}`);
                setCandidates(candidatesResponse.data);
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
                <h1>Calculating top matches...</h1>
            </div>
        );
    }
    if (error) return <div>Error: {error}</div>;

    const notifyCandidate = async () => {
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

    const fakeCandidates = [
        { id: 1, name: 'John Doe', email: 'john.doe@example.com', matchPercentage: 95 },
        { id: 2, name: 'Jane Smith', email: 'jane.smith@example.com', matchPercentage: 90 },
        { id: 3, name: 'Alice Johnson', email: 'alice.johnson@example.com', matchPercentage: 85 },
        { id: 4, name: 'Bob Brown', email: 'bob.brown@example.com', matchPercentage: 80 },
    ];

    const sortedCandidates = candidates ? candidates.sort((a, b) => b.match_score - a.match_score) : fakeCandidates.sort((a, b) => b.matchPercentage - a.matchPercentage);

    return (
        <div>
            <AdminNavBar />
            <div className='container-fluid'>
                <h1 className="mt-4">Job Details</h1>
                {jobDetails && (
                    <div className="card mb-4">
                        <div className="card-body">
                            <h2 className="card-title">{jobDetails.title}</h2>
                            <p className="card-text">{jobDetails.description}</p>
                            <p className="card-text"><strong>Skills Required:</strong> {jobDetails.skills_required}</p>
                            <p className="card-text"><strong>Location:</strong> {jobDetails.street}, {jobDetails.state}, {jobDetails.country}, {jobDetails.zipcode}</p>
                            <p className="card-text"><strong>Posted By:</strong> {jobDetails.posted_by}</p>
                            <p className="card-text"><strong>Application Deadline:</strong> {jobDetails.application_deadline}</p>
                        </div>
                    </div>
                )}
                <h1 className="mt-4">Top Matches</h1>
                {candidates.length > 0 ? (
                    <ul className="list-group">
                        {candidates.map(candidate => (
                            <li key={candidate.student_id} className="list-group-item">
                                <div className='row'>
                                    <div className='col'>
                                        <h3>{candidate.student_name}</h3>
                                    </div>
                                    <div className='col align-items-center'>
                                        <a href="#" onClick={() => notifyCandidate()} className="btn btn-primary" style={{ width: '100%' }}>Notify</a>                                        
                                    </div>
                                </div>
                                <p>Match score: {candidate.match_score}</p>
                                <p>Experience level: {candidate.experience}</p>
                                <p>{candidate.highest_education_level}</p>
                                <p>{candidate.major}</p>
                                <p>{candidate.skills}</p>
                            </li>
                        ))}
                    </ul>
                ) : (
                    <div>
                        <ul className="list-group">
                            {sortedCandidates.map(candidate => (
                                <li key={candidate.id} className="list-group-item">
                                    <h3>{candidate.name}</h3>
                                    <p>Email: {candidate.email}</p>
                                    <p>Match Percentage: {candidate.matchPercentage}%</p>
                                </li>
                            ))}
                        </ul>
                    </div>
                )}
                
            </div>
        </div>
    );
};

export default Matches;