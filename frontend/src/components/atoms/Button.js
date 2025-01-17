import React from 'react';

const Button = ({ type, text }) => (
    <button type={type} className="btn mt-2 btn-danger">
        {text}
    </button>
);

export default Button;