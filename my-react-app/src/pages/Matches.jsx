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
        const fetchJobDetails = async () => {
            try {
                const jobResponse = await api.get(`/jobs/${id}`);
                console.log(jobResponse.data);
                setJobDetails(jobResponse.data);
                
                // const candidatesResponse = await api.get(`/api/jobs/${id}/candidates`);
                // setCandidates(candidatesResponse.data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchJobDetails();
    }, [id]);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;


    const fakeCandidates = [
        { id: 1, name: 'John Doe', email: 'john.doe@example.com', matchPercentage: 95 },
        { id: 2, name: 'Jane Smith', email: 'jane.smith@example.com', matchPercentage: 90 },
        { id: 3, name: 'Alice Johnson', email: 'alice.johnson@example.com', matchPercentage: 85 },
        { id: 4, name: 'Bob Brown', email: 'bob.brown@example.com', matchPercentage: 80 },
    ];

    const sortedCandidates = fakeCandidates.sort((a, b) => b.matchPercentage - a.matchPercentage);

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
                <h1 className="mt-4">Candidate Matches</h1>
                {candidates.length > 0 ? (
                    <ul className="list-group">
                        {candidates.map(candidate => (
                            <li key={candidate.id} className="list-group-item">
                                <h3>{candidate.name}</h3>
                                <p>{candidate.experience}</p>
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