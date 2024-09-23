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
    console.log(email + " " + password);
    var response = await api.post("students/login/", { email, password });
    console.log(response.data);

    // Here we should parse the student_id from the response like so:
    const student_id = response.data.student_id;
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
          <a href="/">
            <img className="logo" src={alpfaLogo} alt=""/>
          </a>
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