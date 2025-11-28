import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';

const Register = () => {
  const [fullName, setFullName] = useState('');
  const [cpfCnpj, setCpfCnpj] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const navigate = useNavigate();

  const handleRegister = (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      alert('As senhas não correspondem!');
      return;
    }
    
    // Simulate storing user data
    const newUser = { fullName, cpfCnpj, email, password };
    localStorage.setItem('user', JSON.stringify(newUser));

    alert('Conta cadastrada com sucesso!');
    navigate('/'); // Redirect to login page
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <h2>Crie sua conta</h2>
        <p>Comece a organizar suas finanças agora mesmo.</p>
        <form onSubmit={handleRegister}>
          <div className="input-group">
            <label htmlFor="fullName">Nome Completo</label>
            <input 
              type="text" 
              id="fullName" 
              placeholder="Seu nome completo" 
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              required
            />
          </div>
          <div className="input-group">
            <label htmlFor="cpfCnpj">CPF/CNPJ</label>
            <input 
              type="text" 
              id="cpfCnpj" 
              placeholder="Seu CPF ou CNPJ" 
              value={cpfCnpj}
              onChange={(e) => setCpfCnpj(e.target.value)}
              required
            />
          </div>
          <div className="input-group">
            <label htmlFor="email">Email</label>
            <input 
              type="email" 
              id="email" 
              placeholder="seuemail@exemplo.com" 
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="input-group">
            <label htmlFor="password">Senha</label>
            <input 
              type="password" 
              id="password" 
              placeholder="Crie uma senha" 
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <div className="input-group">
            <label htmlFor="confirmPassword">Confirmar Senha</label>
            <input 
              type="password" 
              id="confirmPassword" 
              placeholder="Confirme sua senha" 
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="auth-button">Cadastrar</button>
        </form>
        <div className="auth-footer">
          <p>Já tem uma conta? <Link to="/">Faça login</Link></p>
        </div>
      </div>
    </div>
  );
};

export default Register;
