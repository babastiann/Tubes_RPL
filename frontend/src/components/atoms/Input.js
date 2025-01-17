import React from 'react';

const Input = ({ type, name, placeholder, onChange }) => (
    <div className="form-group">
        <input
            type={type}
            name={name}
            placeholder={placeholder}
            className="form-control"
            onChange={onChange}
        />
    </div>
);

export default Input;