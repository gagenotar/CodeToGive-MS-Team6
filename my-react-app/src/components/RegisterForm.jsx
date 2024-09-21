import React from 'react'

import "../css/form.css";
import PropTypes from "prop-types";

export default function LoginForm({fields, onSubmit, onChange}) {
  return (
    <form className="form-submission">
      <div className="subtitle-input-pair">
        <label className="form-subtitle" htmlFor="name">
          Name
        </label>
        <input
          type="text"
          id="name"
          name="name"
          placeholder="Full Name"
          value={fields.name}
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
      <button type="submit" className="btn-form" onSubmit={onSubmit}>
        Sign Up
      </button>
      <div className="footer-section">
        <a href='/login' className="sign-in">Sign In</a>
      </div>
    </form>
  );
}

LoginForm.propTypes = {
  fields: PropTypes.shape({
    email: PropTypes.string,
    password: PropTypes.string,
    name: PropTypes.string
  }),
  onSubmit: PropTypes.func,
  onChange: PropTypes.func,
};