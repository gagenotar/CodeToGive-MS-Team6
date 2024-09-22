import React, { useState, useEffect } from "react";
import api from "../api";
import NavBar from "../components/NavBar";
import "../styles/home.css";
import StudentPublicProfile from "../components/StudentPublicProfile";
import Card from "react-bootstrap/Card";
import Nav from "react-bootstrap/Nav";

const Home = () => {
  const [student, setStudent] = useState({});
  const student_id = localStorage.getItem("student_id");
  const [activeTab, setActiveTab] = useState("#overview");
  const background_color = "#e33940";
  const hover_color = "#820000";
  useEffect(() => {
    const getStudent = async () => {
      const response = await api.get(`/students/${student_id}`);
      setStudent(response.data);
    };

    if (student_id) {
      getStudent();
    }
  }, [student_id]);

  const handleTabClick = (eventKey) => {
    setActiveTab(eventKey);
  };

  return (
    <>
      <NavBar />
      <div className="home-introduction">
        <h1>Home</h1>
        <p>Welcome to the home page, {student.student_name}</p>
      </div>
      <style type="text/css">
        {`
  .nav-pills .nav-link{
    color: #fff;
    background-color: ${background_color};
    border-color: ${background_color};

  }

  .nav-pills .nav-link.active{
    color: #fff;
    background-color: ${hover_color};
  }

  .nav-pills .nav-link:hover {
    background-color: ${hover_color};
  }

  }
    `}
      </style>

      <Card>
        <Card.Header>
          <Nav
            variant="pills"
            defaultActiveKey="#first"
            onSelect={handleTabClick}
            className="center"
          >
            <Nav.Item variant="red">
              <Nav.Link eventKey="#overview" className="primary">
                Overview
              </Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="#matched-jobs" className="primary">
                Matched Jobs
              </Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="#notifications">Notifcations</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="#event">Events</Nav.Link>
            </Nav.Item>
          </Nav>
        </Card.Header>
        {activeTab == "#overview" && <StudentPublicProfile student={student} />}
      </Card>
    </>
  );
};

export default Home;
