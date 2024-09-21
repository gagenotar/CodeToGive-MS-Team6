import React, { useState, useEffect } from 'react';
import api from '../api';
import AdminNavBar from '../components/AdminNavBar';

const Admin = () => {
    const [admin, setAdmin] = useState({});
    const jobadmin_id = localStorage.getItem('jobadmin_id');

    useEffect(() => {
        const getAdmin = async () => {
            const response = await api.get(`/job_admin/${jobadmin_id}`);
            setAdmin(response.data);
        };

        if (jobadmin_id) {
            getAdmin();
        }
    }, [jobadmin_id]);

    return (
      <div>
        <AdminNavBar />
        <h1>Home</h1>
        <p>Welcome to the admin page, {admin.name}</p>
        <div class="container" id='home-wrapper'>
            <div class="row mb-3">
              <div class="col">
                <a href="/jobs" class="btn btn-primary">View Jobs</a>
              </div>
            </div>
            <div class="row mb-3">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">Profile</h5>
                            {admin && (
                                <div>
                                    <p>{admin.name}</p>
                                    <p>{admin.email}</p>
                                </div>
                            )}
                            <a href="/jobs" class="btn btn-primary">View Jobs</a>
                            
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

export default Admin