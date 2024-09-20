import React, { useState } from 'react';
import Form from '../components/Form';
import api from '../api';

function Login() {
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
        const response = await api.post('/login/', { email, password });
        console.log(response.data);
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