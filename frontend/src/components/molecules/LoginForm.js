import React from 'react';
import Button from '../atoms/Button';

const LoginForm = ({ onSubmit, onChange }) => (
    <form onSubmit={onSubmit} className="login-form">
        <div className="form-group">
            <label htmlFor="username">Username:</label>
            <input type="text" name="username" className="form-control" onChange={onChange} required />
        </div>
        <div className="form-group">
            <label htmlFor="password">Password:</label>
            <input type="password" name="password" className="form-control" onChange={onChange} required />
        </div>
        <Button type="submit" text="Login" />
    </form>
);

export default LoginForm;