import React, { useState, useEffect } from 'react';
import Login from './components/Login';
import Register from './components/Register';
import Profile from './components/Profile';
import { auth } from './firebase'; // Assuming you have firebase configured

function App() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [showRegister, setShowRegister] = useState(false);

  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged(user => {
      setUser(user);
      setLoading(false);
    });
    return () => unsubscribe();
  }, []);

  if (loading) {
    return <div>Carregando...</div>;
  }

  const handleLogin = () => {
    // This will be handled by onAuthStateChanged
  };

  const handleRegister = () => {
    setShowRegister(false);
  };

  const handleShowRegister = () => {
    setShowRegister(true);
  };

  const handleShowLogin = () => {
    setShowRegister(false);
  };

  if (!user) {
    return (
      <div>
        {showRegister ? (
          <Register onRegister={handleRegister} onShowLogin={handleShowLogin} />
        ) : (
          <Login onLogin={handleLogin} onShowRegister={handleShowRegister} />
        )}
      </div>
    );
  }

  return <Profile user={user} />;
}

export default App;