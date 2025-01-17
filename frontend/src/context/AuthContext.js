import React, { createContext, useState } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [authState, setAuthState] = useState({
        isAuthenticated: false,
        userLevel: null,
        token: null,
    });

    const login = (userLevel, token) => {
        setAuthState({
            isAuthenticated: true,
            userLevel: userLevel,
            token: token,
        });
    };

    const logout = () => {
        setAuthState({
            isAuthenticated: false,
            userLevel: null,
            token: null,
        });
    };

    return (
        <AuthContext.Provider value={{ authState, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};