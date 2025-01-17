import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

const PrivateRoute = ({ component: Component }) => {
    const { authState } = useContext(AuthContext);

    return authState.isAuthenticated ? <Component /> : <Navigate to="/" />;
};

export default PrivateRoute;