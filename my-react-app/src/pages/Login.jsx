import React, { useState } from "react";
import api from "../api";
import alpfaLogo from "../img/alpfaLogo.png";
import LoginForm from "../components/LoginForm";

const Login = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Handle registration logic here
    const email = e.target.email.value;
    const password = e.target.password.value;
    var response = await api.post("/login/", { email, password });
    console.log(response.data);

        // Here we should parse the student_id from the response like so:
        const student_id = response.data.student_id;

        // We should also parse the role from the response like so:
        // const role = response.data.role;
        // For now we will hardcode the role to 'student' or 'admin'
        // const role = 'student';
        const role = 'admin';

    localStorage.setItem("student_id", student_id);
    window.location.href = "/home";
  };
  const fields = {
    email: formData.email,
    password: formData.password,
  };

  return (

      <div className="background-color">
        <div className="form-header">
          <div className="title">Welcome! Login</div>
          <img className="logo" src={alpfaLogo} alt="" />
        </div>
        <LoginForm
          fields={fields}
          onSubmit={handleSubmit}
          onChange={handleChange}
        />
      </div>
 
  );
};

export default Login;
