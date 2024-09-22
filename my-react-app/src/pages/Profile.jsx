import React, { useEffect, useState } from "react";
import api from "../api";
import NavBar from "../components/NavBar";

import "../styles/profile.css";
import ProfileInfo from "../components/ProfileInfo";
const Profile = () => {
  const [studentData, setStudentData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const student_id = localStorage.getItem("student_id");

  useEffect(() => {
    const fetchStudentData = async () => {
      try {
        const response = await api.get(`/students/${student_id}`);
        setStudentData(response.data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchStudentData();
  }, [student_id]);

  const handleChange = (event) => {
    setStudentData({ ...studentData, [event.target.name]: event.target.value });
  };

  const handleBtnClick = async () => {
    const student_id = localStorage.getItem("student_id");
    console.log({ ...studentData, ["university"]: "" });
    try {
      //university is not availlable in get request for student
      const response = await api.post(`/students/update/${student_id}`, {
        ...studentData,
        ["university"]: "",
      });
      console.log("Response:", response.data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <>
      <NavBar />
      <div className="profile-info">
      <h1 className="profile-title">Profile</h1>
      {studentData && (
        <ProfileInfo
          studentData={studentData}
          onClick={handleBtnClick}
          onChange={handleChange}
        />
      )}
      </div>
    </>
  );
};

export default Profile;
