import React, { useState } from 'react';
import Form from '../components/Form';
import api from '../api';

function Register() {
    const [formData, setFormData] = useState({
        student_name: '',
        email: '',
        password: ''
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        // Handle registration logic here
        const email = e.target.email.value;
        const password = e.target.password.value;
        const student_name = e.target.student_name.value;
        const response = await api.post('/students/register', { student_name, email, password });
        console.log(response.data);
    };

    const fields = [
        { label: 'Student Name', type: 'text', name: 'student_name', value: formData.student_name, onChange: handleChange },
        { label: 'Email', type: 'text', name: 'email', value: formData.email, onChange: handleChange },
        { label: 'Password', type: 'password', name: 'password', value: formData.password, onChange: handleChange }
    ];

    return (
        <>
            <h1>Register</h1>
            <Form fields={fields} onSubmit={handleSubmit} buttonText="register" />
        </>
    );
}

export default Register;