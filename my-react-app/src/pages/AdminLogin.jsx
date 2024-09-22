import React, { useState } from "react";
import api from "../api";
import alpfaLogo from "../img/alpfaLogo.png";
import AdminLoginForm from "../components/AdminLoginForm";

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
    var response = await api.post("/job_admin/login/", { email, password });
    console.log(response.data);

    // Here we should parse the jobadmin_id from the response like so:
    // const jobadmin_id = response.data.job_admin_id;
    const jobadmin_id = 1;
    localStorage.setItem("jobadmin_id", jobadmin_id);
    
    window.location.href = "/admin";
  };

  const fields = {
    email: formData.email,
    password: formData.password,
  };

  return (
      <div className="background-color">
        <div className="form-header">
          <div className="title">Welcome Admin! Login</div>
          <img className="logo" src={alpfaLogo} alt="" />
        </div>
        <AdminLoginForm
          fields={fields}
          onSubmit={handleSubmit}
          onChange={handleChange}
        />
      </div>
 
  );
};

export default Login;