import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft, Edit3, Save, Camera, ShieldCheck, MapPin, MessageSquare } from 'lucide-react';
import './Profile.css';

const Profile = () => {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [profilePic, setProfilePic] = useState(null);
  const [initials, setInitials] = useState('');

  useEffect(() => {
    const storedUser = JSON.parse(localStorage.getItem('user'));
    if (storedUser) {
      setUser(storedUser);
      const nameParts = storedUser.fullName.split(' ');
      const firstInitial = nameParts[0] ? nameParts[0][0] : '';
      const lastInitial = nameParts.length > 1 ? nameParts[nameParts.length - 1][0] : '';
      setInitials(`${firstInitial}${lastInitial}`.toUpperCase());

      const storedPic = localStorage.getItem(`${storedUser.email}_profilePic`);
      if (storedPic) setProfilePic(storedPic);
    }
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUser(prev => ({ ...prev, [name]: value }));
  };

  const handleSave = () => {
    localStorage.setItem('user', JSON.stringify(user));
    setIsEditing(false);
    alert('Perfil atualizado com sucesso!');
  };

  const handleProfilePicChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (upload) => {
        const newPic = upload.target.result;
        setProfilePic(newPic);
        localStorage.setItem(`${user.email}_profilePic`, newPic);
      };
      reader.readAsDataURL(file);
    }
  };

  if (!user) return <div>Carregando...</div>;

  return (
    <div className="profile-view">
        <div className="view-header">
            <button onClick={() => navigate('/home')} className="back-button"><ArrowLeft size={24} /></button>
            <h2>Meu Perfil</h2>
        </div>
        <div className="profile-card">
            <div className="profile-picture-section">
                <div className="profile-picture-wrapper">
                    {profilePic ? (
                        <img src={profilePic} alt="Foto de Perfil" className="profile-picture" />
                    ) : (
                        <div className="initials-avatar">{initials}</div>
                    )}
                    <label htmlFor="profilePicInput" className="profile-pic-edit-button">
                        <Camera size={18} />
                    </label>
                    <input id="profilePicInput" type="file" accept="image/*" onChange={handleProfilePicChange} style={{ display: 'none' }}/>
                </div>
            </div>

            <div className="profile-info">
                <ProfileField label="Nome Completo" value={user.fullName} readOnly />
                <ProfileField label="CPF/CNPJ" value={user.cpfCnpj} readOnly />
                <ProfileField label="Email" name="email" value={user.email} onChange={handleInputChange} isEditing={isEditing} />
                <ProfileField label="Telefone" name="phone" value={user.phone || ''} placeholder="Adicionar telefone" onChange={handleInputChange} isEditing={isEditing} />
            </div>

            <div className="profile-actions">
                {isEditing ? (
                    <button className="profile-save-button" onClick={handleSave}><Save size={20}/> Salvar Alterações</button>
                ) : (
                    <button className="profile-edit-button" onClick={() => setIsEditing(true)}><Edit3 size={20}/> Editar Perfil</button>
                )}
                <button className="profile-action-button" onClick={() => alert('Funcionalidade de endereço em desenvolvimento.')}><MapPin size={20}/> Adicionar Endereço</button>
            </div>

            <div className="profile-footer">
                <ShieldCheck size={18} />
                <p>Seus dados pessoais são protegidos pela LGPD.</p>
            </div>
        </div>
        <button className="chat-bubble-button" onClick={() => alert('Funcionalidade de chat em desenvolvimento.')}>
            <MessageSquare size={28} />
        </button>
    </div>
  );
};

const ProfileField = ({ label, value, name, onChange, isEditing, readOnly, placeholder }) => (
    <div className="profile-field">
        <label>{label}</label>
        <input 
            type="text" 
            name={name}
            value={value}
            readOnly={!isEditing || readOnly}
            onChange={onChange}
            placeholder={placeholder}
            className={!isEditing || readOnly ? 'read-only' : ''}
        />
    </div>
);

export default Profile;
