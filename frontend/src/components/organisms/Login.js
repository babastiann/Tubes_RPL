import React, { useState, useContext } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import LoginForm from '../molecules/LoginForm';
import { AuthContext } from '../../context/AuthContext';
import './Login.css';

const Login = () => {
    const [form, setForm] = useState({ username: '', password: '' });
    const navigate = useNavigate();
    const { login } = useContext(AuthContext);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!form.username || !form.password) {
            toast.error('All fields are required!', {
                position: "top-right",
                autoClose: 5000,
                hideProgressBar: false,
                closeOnClick: true,
                pauseOnHover: true,
                draggable: true,
                progress: undefined,
            });
            return;
        }
        try {
            const response = await axios.post('http://127.0.0.1:5000/login', form);
            const { user_level, token } = response.data;
            login(user_level, token);
            navigate('/dashboard');
        } catch (error) {
            toast.error('Login failed: Invalid credentials!', {
                position: "top-right",
                autoClose: 5000,
                hideProgressBar: false,
                closeOnClick: true,
                pauseOnHover: true,
                draggable: true,
                progress: undefined,
            });
        }
    };

    return (
        <div className="login-container d-flex justify-content-center align-items-center">
            <div className="login-card card">
                <div className="card-body">
                    <h1 className="card-title text-center">Login</h1>
                    <LoginForm onSubmit={handleSubmit} onChange={handleChange} />
                </div>
            </div>
            <ToastContainer />
        </div>
    );
};

export default Login;