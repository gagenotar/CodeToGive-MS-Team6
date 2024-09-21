import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const Matches = () => {
    const { id } = useParams();
    const [jobDetails, setJobDetails] = useState(null);
    const [candidates, setCandidates] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchJobDetails = async () => {
            try {
                const jobResponse = await axios.get(`/api/jobs/${id}`);
                setJobDetails(jobResponse.data);
                
                const candidatesResponse = await axios.get(`/api/jobs/${id}/candidates`);
                setCandidates(candidatesResponse.data);
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

    return (
        <div>
            <h1>Job Details</h1>
            {jobDetails && (
                <div>
                    <h2>{jobDetails.title}</h2>
                    <p>{jobDetails.description}</p>
                </div>
            )}
            <h1>Candidate Matches</h1>
            {candidates.length > 0 ? (
                <ul>
                    {candidates.map(candidate => (
                        <li key={candidate.id}>
                            <h3>{candidate.name}</h3>
                            <p>{candidate.experience}</p>
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No candidates found</p>
            )}
        </div>
    );
};

export default Matches;