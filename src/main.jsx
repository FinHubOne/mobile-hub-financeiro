
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { MainApp } from './App.jsx';
import Login from './components/Login.jsx';
import Register from './components/Register.jsx';
import './index.css';
import './components/Auth.css';
import './components/Profile.css';

// Basic function to check for a simulated token
const isAuthenticated = () => !!localStorage.getItem('authToken');

const PrivateRoute = ({ children }) => {
  return isAuthenticated() ? children : <Navigate to="/" />;
};

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route 
          path="/home" 
          element={<PrivateRoute><MainApp /></PrivateRoute>} 
        />
        <Route 
          path="/analysis" 
          element={<PrivateRoute><MainApp /></PrivateRoute>} 
        />
        <Route 
          path="/wallet" 
          element={<PrivateRoute><MainApp /></PrivateRoute>} 
        />
        <Route 
          path="/profile" 
          element={<PrivateRoute><MainApp /></PrivateRoute>} 
        />
        {/* Redirect any other path to login or home depending on auth status */}
        <Route path="*" element={<Navigate to={isAuthenticated() ? '/home' : '/'} />} />
      </Routes>
    </Router>
  </React.StrictMode>
);
