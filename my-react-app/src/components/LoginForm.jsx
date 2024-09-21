import React from 'react'

import "../styles/form.css";
import PropTypes from "prop-types";

export default function LoginForm({fields, onSubmit, onChange}) {
  return (

      <form className="form-submission">
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
          Login
        </button>
        <div className="footer-section">
          <div className="dont-have-an-account">
            Don&apos;t have an account?
          </div>
          <a href="/register" className="sign-up">Sign Up</a>
        </div>
      </form>
    
  );
}

LoginForm.propTypes = {
  fields: PropTypes.shape({
    email: PropTypes.string,
    password: PropTypes.string,
  }),
  onSubmit: PropTypes.func.isRequired,
  onChange: PropTypes.func,
};