import React, { useEffect, useState } from 'react';
import api from '../api';
import NavBar from '../components/NavBar';

const Profile = () => {
    const [studentData, setStudentData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [isEditing, setIsEditing] = useState(false);
    const [formData, setFormData] = useState({
        experience: 0,
        highest_education_level: '',
        major: '',
        skills: '',
        street: '',
        state: '',
        country: '',
        zipcode: ''
    });

    const student_id = localStorage.getItem('student_id');

    useEffect(() => {
        const fetchStudentData = async () => {
            try {
                const response = await api.get(`/students/${student_id}`);
                setStudentData(response.data);
                setFormData({
                    experience: response.data.experience || 0,
                    highest_education_level: response.data.highest_education_level || '',
                    major: response.data.major || '',
                    skills: response.data.skills || '',
                    street: response.data.street || '',
                    state: response.data.state || '',
                    country: response.data.country || '',
                    zipcode: response.data.zipcode || ''
                });
            } catch (err) {
                setError(err);
            } finally {
                setLoading(false);
            }
        };

        fetchStudentData();
    }, [student_id]);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSave = async () => {
        try {
            const response = await api.post(`/students/update/${student_id}`, formData);
            console.log(response.data);
            setStudentData({
                ...studentData,
                ...formData
            });
            setIsEditing(false);
        } catch (err) {
            setError(err);
        }
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    return (
        <div>
            <NavBar />
            <div className="mt-4">
                <h1 className="m-4">Profile Page</h1>
                {studentData && (
                    <div className="card m-4">
                        <div className="card-body">
                            <p><strong>Name:</strong> {studentData.student_name}</p>
                            <p><strong>Email:</strong> {studentData.email}</p>
                            {isEditing ? (
                                <div>
                                    <div className="form-group">
                                        <label>Experience:</label>
                                        <input
                                            type="number"
                                            className="form-control"
                                            name="experience"
                                            value={formData.experience}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="form-group">
                                        <label>Highest Education Level:</label>
                                        <input
                                            type="text"
                                            className="form-control"
                                            name="highest_education_level"
                                            value={formData.highest_education_level}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="form-group">
                                        <label>Major:</label>
                                        <input
                                            type="text"
                                            className="form-control"
                                            name="major"
                                            value={formData.major}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="form-group">
                                        <label>Skills:</label>
                                        <input
                                            type="text"
                                            className="form-control"
                                            name="skills"
                                            value={formData.skills}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="form-group">
                                        <label>Street:</label>
                                        <input
                                            type="text"
                                            className="form-control"
                                            name="street"
                                            value={formData.street}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="form-group">
                                        <label>State:</label>
                                        <input
                                            type="text"
                                            className="form-control"
                                            name="state"
                                            value={formData.state}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="form-group">
                                        <label>Country:</label>
                                        <input
                                            type="text"
                                            className="form-control"
                                            name="country"
                                            value={formData.country}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <div className="form-group">
                                        <label>Zipcode:</label>
                                        <input
                                            type="text"
                                            className="form-control"
                                            name="zipcode"
                                            value={formData.zipcode}
                                            onChange={handleInputChange}
                                        />
                                    </div>
                                    <button className="btn btn-primary mt-3" onClick={handleSave}>Save</button>
                                </div>
                            ) : (
                                <div>
                                    <p><strong>Experience:</strong> {studentData.experience}</p>
                                    <p><strong>Highest Education Level:</strong> {studentData.highest_education_level}</p>
                                    <p><strong>Major:</strong> {studentData.major}</p>
                                    <p><strong>Skills:</strong> {studentData.skills}</p>
                                    <p><strong>Street:</strong> {studentData.street}</p>
                                    <p><strong>State:</strong> {studentData.state}</p>
                                    <p><strong>Country:</strong> {studentData.country}</p>
                                    <p><strong>Zipcode:</strong> {studentData.zipcode}</p>
                                    <button className="btn btn-secondary mt-3" onClick={() => setIsEditing(true)}>Edit</button>
                                </div>
                            )}
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Profile;