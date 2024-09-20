import React, { useState } from 'react';
import api from '../api';
import RegisterForm from "../components/RegisterForm"
import alpfaLogo from "../img/alpfaLogo.png";
const Register = () => {
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


    const fields = {
        email: formData.email, 
        name: formData.name,
        password: formData.password
    }


    return (
      <div className="background-color">
        <div className="form-header">
          <div className="title">Sign Up</div>
          <img className="logo" src={alpfaLogo} alt="" />
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