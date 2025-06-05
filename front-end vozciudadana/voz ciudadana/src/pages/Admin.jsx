import React, { useEffect, useState } from 'react';
import './Admin.css';
import CardAdmin from '../components/Admin/CardAdmin';

const Admin = () => {
  const [datos, setDatos] = useState({
    publicaciones: 0,
    usuarios: 0,
    encuestas: 0,
  });

  useEffect(() => {
   
    setDatos({
      publicaciones: 12,
      usuarios: 8,
      encuestas: 5,
    });
  }, []);

  return (
    <div className="admin-container">
      <h1 className="admin-title">Panel del Administrador</h1>
      <div className="admin-grid">
        <CardAdmin tipo="Publicaciones" cantidad={datos.publicaciones} color="#4f46e5" />
        <CardAdmin tipo="Usuarios" cantidad={datos.usuarios} color="#059669" />
        <CardAdmin tipo="Encuestas" cantidad={datos.encuestas} color="#d97706" />
      </div>

      <div className="admin-actions">
        <button className="admin-btn">Ver publicaciones reportadas</button>
        <button className="admin-btn">Gestionar usuarios</button>
        <button className="admin-btn">Revisar encuestas</button>
      </div>
    </div>
  );
};

export default Admin;