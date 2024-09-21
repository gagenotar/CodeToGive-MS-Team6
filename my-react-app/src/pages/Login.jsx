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
        const student_id = response.data.student_id;

        // We should also parse the role from the response like so:
        // const role = response.data.role;
        // For now we will hardcode the role to 'student' or 'admin'
        // const role = 'student';
        const role = 'admin';

        localStorage.setItem('student_id', student_id);

        if (role === 'admin') {
            window.location.href = '/admin';
        } else {
            window.location.href = '/home'; 
        }
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