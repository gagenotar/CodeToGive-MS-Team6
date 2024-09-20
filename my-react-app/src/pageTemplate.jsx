import React, {useState, useEffect} from 'react';
import api from './api';

const pageTemplate = () => {
    const [params, setParams] = useState([]);

    const fetchParams = async () => {
        const response = await api.get('/endpoint/');
        setParams(response.data);
    };

    useEffect(() => {
        fetchParams();
    }, []);

    const handleEvent = (e) => {
        e.preventDefault();
        fetchParams();
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await api.post('/endpoint/', {name: e.target.name.value});
        setParams([...params, response.data]);
    }

    return (
        <div>
            <nav className="navbar">
                <div className="container-fluid">
                    <a className="navbar-brand" href="#">Navbar</a>
                </div>
            </nav>
            <h1>Params</h1>
            <ul>
                {params.map((param) => (
                    <li key={param.id}>{param.name}</li>
                ))}
            </ul>
            <button onClick={handleEvent}>Refresh</button>
            <form onSubmit={handleSubmit}>
                <input type="text" name="name" />
                <button type="submit">Add</button>
            </form>
        </div>
    );
}

export default pageTemplate;