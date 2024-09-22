import React, { useState } from 'react';
import api from '../api';
import AdminNavBar from '../components/AdminNavBar';

const Events = () => {
    const jobadmin_id = parseInt(localStorage.getItem('jobadmin_id'), 10);
    const [event, setEvent] = useState({
        event_name: '',
        event_type: '',
        description: '',
        sponsor_id: jobadmin_id
    });

    const [message, setMessage] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setEvent({
            ...event,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await api.post('/events', event);
            if (response.status === 200) {
                setMessage('Event posted successfully!');
                // Clear the form
                setEvent({
                    event_name: '',
                    event_type: '',
                    description: '',
                    sponsor_id: jobadmin_id
                });
            } else {
                setMessage('Failed to post event.');
            }
        } catch (error) {
            setMessage('Failed to post event.');
        }
    };

    return (
        <div>
            <AdminNavBar />
            <div className='events-wrapper'>
                <div className="card m-5">
                    <h1>Create an Event</h1>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label htmlFor="event_name" className="form-label">Event Name</label>
                            <input type="text" className="form-control" id="event_name" name="event_name" value={event.event_name} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="event_type" className="form-label">Event Type</label>
                            <input type="text" className="form-control" id="event_type" name="event_type" value={event.event_type} onChange={handleChange} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="description" className="form-label">Description</label>
                            <textarea className="form-control" id="description" name="description" value={event.description} onChange={handleChange} required />
                        </div>
                        <button type="submit" className="btn btn-primary">Submit</button>
                    </form>
                    {message && <p className="mt-3">{message}</p>}
                </div>
            </div>
        </div>
    );
};

export default Events;
