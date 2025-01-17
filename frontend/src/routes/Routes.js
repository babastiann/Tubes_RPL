import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Login from '../components/organisms/Login';
import Dashboard from '../components/pages/Dashboard';
import ErrorPage from '../components/pages/ErrorPage';
import { AuthProvider } from '../context/AuthContext';
import PrivateRoute from '../components/PrivateRoute';

const AppRoutes = () => (
    <Router>
        <AuthProvider>
            <Routes>
                <Route exact path="/" element={<Login />} />
                <Route path="/dashboard" element={<PrivateRoute component={Dashboard} />} />
                <Route path="/error" element={<ErrorPage />} />
                <Route path="*" element={<Navigate to="/error" state={{ error: 404 }} />} />
            </Routes>
        </AuthProvider>
    </Router>
);

export default AppRoutes;