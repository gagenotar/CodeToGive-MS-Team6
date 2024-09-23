import React, { useState, useEffect } from 'react';
import api from '../api';
import NavBar from '../components/NavBar';

const Admin = () => {
    const [admin, setAdmin] = useState({});
    const student_id = localStorage.getItem('student_id');

    useEffect(() => {
        const getAdmin = async () => {
            const response = await api.get(`/students/${student_id}`);
            setAdmin(response.data);
        };

        if (student_id) {
            getAdmin();
        }
    }, [student_id]);

    return (
      <div>
        <NavBar />
        <h1>Admin</h1>
        <p>Welcome to the admin page, {admin.student_name}</p>
      </div>
    )
}

export default Admin