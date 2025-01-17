import React from 'react';
import { useLocation } from 'react-router-dom';

const ErrorPage = () => {
    const location = useLocation();
    const { state } = location;

    const getErrorMessage = () => {
        if (state && state.error) {
            switch (state.error) {
                case 401:
                    return 'Unauthorized access. Please log in.';
                case 404:
                    return 'Page not found.';
                case 500:
                    return 'Internal server error. Please try again later.';
                default:
                    return 'An unknown error occurred.';
            }
        }
        return 'An unknown error occurred.';
    };

    return (
        <div>
            <h1>Error</h1>
            <p>{getErrorMessage()}</p>
        </div>
    );
};

export default ErrorPage;