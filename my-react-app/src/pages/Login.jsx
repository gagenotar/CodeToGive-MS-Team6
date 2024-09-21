import React, { useState } from 'react';
import Form from '../components/Form';
import api from '../api';

const Login = () => {
    const [formData, setFormData] = useState({
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
        var response = await api.post('/login/', { email, password });
        console.log(response.data);

        // Here we should parse the student_id from the response like so:
        // student_id = response.data.student_id;
        // For now we will just hardcode the student_id to 1
        const student_id = 1;

        localStorage.setItem('student_id', student_id);
        window.location.href = '/home'; 
    };

    const fields = [
        { label: 'Email', type: 'text', name: 'email', value: formData.email, onChange: handleChange },
        { label: 'Password', type: 'password', name: 'password', value: formData.password, onChange: handleChange }
    ];

    return (
        <>
            <h1>Login</h1>
            <Form fields={fields} onSubmit={handleSubmit} buttonText="login" />
        </>
    );
}

export default Login;