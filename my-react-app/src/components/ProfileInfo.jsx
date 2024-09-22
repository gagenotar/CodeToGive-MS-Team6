//Edits Student's Information 



import React from 'react'
import Button from "react-bootstrap/Button";

const ProfileInfo = ({ studentData, onChange, onClick }) => {
  return (
    <div className="profile-info">
      <div className="section">
        <div className="input-group mb-3">
          <span className="input-group-text input-appearance" id="basic-addon1">
            Name
          </span>
          <input
            type="text"
            className="form-control input-appearance"
            value={studentData.student_name}
            name="student_name"
            aria-label="Name"
            aria-describedby="basic-addon1"
            onChange={onChange}
          />
        </div>
        <div className="input-group mb-3">
          <span className="input-group-text input-appearance" id="basic-addon1">
            Email
          </span>
          <input
            type="text"
            className="form-control input-appearance"
            name="email"
            value={studentData.email}
            aria-label="Email"
            aria-describedby="basic-addon1"
            onChange={onChange}
          />
        </div>
        <div className="input-group mb-3">
          <span className="input-group-text input-appearance" id="basic-addon1">
            Experience
          </span>
          <input
            type="text"
            className="form-control input-appearance"
            value={studentData.experience}
            name="experience"
            aria-label="Experience"
            aria-describedby="basic-addon1"
          />
        </div>
        <div className="input-group mb-3">
          <span className="input-group-text input-appearance" id="basic-addon1">
            Highest Education Level
          </span>
          <input
            type="text"
            className="form-control input-appearance"
            value={studentData.highest_education_level}
            name="highest_education_level"
            aria-label="Username"
            aria-describedby="basic-addon1"
            onChange={onChange}
          />
        </div>
        <div className="input-group mb-3">
          <span className="input-group-text input-appearance">Skills</span>
          <textarea
            className="form-control input-appearance"
            aria-label="Skills"
            value={studentData.skills}
            name="skills"
            onChange={onChange}
          ></textarea>
        </div>

        <div className="input-group mb-3">
          <span className="input-group-text input-appearance">Address</span>
          <input
            type="text"
            className="form-control input-appearance"
            aria-label="Street"
            value={studentData.street}
            name="street"
            onChange={onChange}
          />
        </div>
        <div className="input-group mb-3">
          <span className="input-group-text input-appearance">Zip Code</span>
          <input
            type="text"
            className="form-control input-appearance"
            aria-label="Zip Code"
            value={studentData.zipcode}
            name="zipcode"
            onChange={onChange}
          />
        </div>
        <div className="input-group mb-3">
          <span className="input-group-text input-appearance">State</span>
          <input
            type="text"
            className="form-control input-appearance"
            aria-label="State"
            name="state"
            value={studentData.state}
            onChange={onChange}
          />
        </div>
        <div className="input-group mb-3">
          <span className="input-group-text input-appearance">Country</span>
          <input
            type="text"
            className="form-control input-appearance"
            aria-label="Country"
            value={studentData.country}
            name="country"
            onChange={onChange}
          />
        </div>
      </div>
      <div className="btn-section">
        <Button variant="primary" onClick={onClick}>
          Save
        </Button>
      </div>
    </div>
  );
};

export default ProfileInfo;