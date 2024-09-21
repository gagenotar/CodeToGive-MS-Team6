import React, { useEffect, useState } from 'react';
import api from '../api';
import NavBar from '../components/NavBar';

const Profile = () => {
    const [studentData, setStudentData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    const student_id = localStorage.getItem('student_id');

    useEffect(() => {
        const fetchStudentData = async () => {
            try {
                const response = await api.get(`/students/${student_id}`);
                setStudentData(response.data);
            } catch (err) {
                setError(err);
            } finally {
                setLoading(false);
            }
        };

        fetchStudentData();
    }, [student_id]);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    return (
        <div>
            <NavBar />
            <h1>Profile Page</h1>
            {studentData && (
                <div>
                    <p>Name: {studentData.student_name}</p>
                    <p>Email: {studentData.email}</p>
                    <p>ID: {studentData.student_id}</p>
                    {/* Add more fields as necessary */}
                </div>
            )}
        </div>
    );
};

export default Profile;