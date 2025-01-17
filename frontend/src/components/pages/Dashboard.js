import React, { useContext } from 'react';
import { AuthContext } from '../../context/AuthContext';

const Dashboard = () => {
    const { authState } = useContext(AuthContext);

    return (
        <div className="container">
            <h1>Dashboard</h1>
            {authState.userLevel === 1 && (
                <div>
                    <h2>Admin Dashboard</h2>
                    <p>Welcome to the admin dashboard!</p>
                    {/* Add admin-specific content here */}
                </div>
            )}
            {authState.userLevel === 2 && (
                <div>
                    <h2>Special User Dashboard</h2>
                    <p>Welcome to the special user dashboard!</p>
                    {/* Add special user-specific content here */}
                </div>
            )}
            {authState.userLevel === 3 && (
                <div>
                    <h2>User Dashboard</h2>
                    <p>Welcome to the user dashboard!</p>
                    {/* Add user-specific content here */}
                </div>
            )}
        </div>
    );
};

export default Dashboard;