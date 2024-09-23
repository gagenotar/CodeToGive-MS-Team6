import React, { useState } from 'react';
import api from '../api';
import alpfaLogo from "../img/alpfaLogo.png";
import RegisterForm from "../components/RegisterForm"

const Register = () => {
    const [formData, setFormData] = useState({
        name: '',
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
        const student_name = e.target.name.value;
        const response = await api.post('/students/register', { student_name, email, password });
        console.log(response.data);

        if (response.status === 200) {
            window.location.href = '/login';
        } else {
            alert('Registration failed');
        }
    };


    const fields = {
        email: formData.email, 
        name: formData.name,
        password: formData.password
    }


    return (
      <div className="background-color">
        <div className="form-header">
          <div className="title">Sign Up</div>
          <a href="/">
            <img className="logo" src={alpfaLogo} alt=""/>
          </a>
        </div>
        <RegisterForm
          fields={fields}
          onSubmit={handleSubmit}
          onChange={handleChange}
        />
      </div>
    );
}

export default Register;