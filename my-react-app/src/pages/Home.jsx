import React, { useState, useEffect } from 'react';
import api from '../api';
import NavBar from '../components/NavBar';
import '../styles/Home.css';

const Home = () => {

    const [student, setStudent] = useState({});
    const student_id = localStorage.getItem('student_id');

    useEffect(() => {
        const getStudent = async () => {
            const response = await api.get(`/students/${student_id}`);
            setStudent(response.data);
        };

        if (student_id) {
            getStudent();
        }
    }, [student_id]);

    return (
      <div>
        <NavBar />
        <h1>Home</h1>
        <p>Welcome to the home page, {student.student_name}</p>
        <div class="container" id='home-wrapper'>
            <div class="row mb-3">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">Profile</h5>
                            {student && (
                                <div>
                                    <p>{student.student_name}</p>
                                    <p>{student.email}</p>
                                    <p>Experience Level: {student.experience}</p>
                                    <p>{student.major}</p>
                                    <p>{student.university}</p>
                                </div>
                            )}
                            <a href="/profile" class="btn btn-primary">View Profile</a>
                            
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">Matched Jobs</h5>
                            <p class="card-text">List of matched jobs</p>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">Notification</h5>
                            <p class="card-text">List of notifications</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row mb-3 justify-content-center">
                <div class="col-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">Events</h5>
                            <p class="card-text">List of events</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>
      )
}

export default Home