import React, { useState, useEffect } from 'react';
import api from '../api';
import NavBar from '../components/NavBar';

const Home = () => {
    const [student, setStudent] = useState({});
    const student_id = localStorage.getItem('student_id');

    useEffect(() => {
        const getStudent = async () => {
            const response = await api.get(`/students/${student_id}`);
            setStudent(response.data);
        };

        if (student_id) {
            getStudent();
        }
    }, [student_id]);

    return (
      <div>
        <NavBar />
        <h1>Home</h1>
        <p>Welcome to the home page, {student.student_name}</p>
      </div>
      )
}

export default Home