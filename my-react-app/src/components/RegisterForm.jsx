import React from 'react';
import "../styles/form.css";
import PropTypes from "prop-types";

export default function RegisterForm({fields, onSubmit, onChange}) {
  return (
      <form className="form-submission" onSubmit={onSubmit}>
        <div className="subtitle-input-pair">
          <label className="form-subtitle" htmlFor="name">
            Name
          </label>
          <input
            type="text"
            id="name"
            name="name"
            placeholder="Full name"
            value={fields.student_name}
            onChange={onChange}
            required
          />
        </div>
        <div className="subtitle-input-pair">
          <label className="form-subtitle" htmlFor="email">
            Email
          </label>
          <input
            type="email"
            id="email"
            name="email"
            placeholder="Email"
            value={fields.email}
            onChange={onChange}
            required
          />
        </div>
        <div className="subtitle-input-pair">
          <label className="form-subtitle" htmlFor="password">
            Password
          </label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Password"
            value={fields.password}
            onChange={onChange}
            required
          />
        </div>
        <button type="submit" className="btn-form">
          Register
        </button>
        <div className="footer-section">
          <div className="already-have-an-account">
            Already have an account?
          </div>
          <a href="/login" className="sign-in">Sign In</a>
        </div>
      </form>
  );
}

RegisterForm.propTypes = {
  fields: PropTypes.shape({
    email: PropTypes.string,
    password: PropTypes.string,
    confirmPassword: PropTypes.string,
  }),
  onSubmit: PropTypes.func.isRequired,
  onChange: PropTypes.func,
};