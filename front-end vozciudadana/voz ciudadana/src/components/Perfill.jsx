import React from 'react';

const Perfill = () => {
    return (
        <div className="perfil-container">
            <div className="perfil-header">
                <img
                    
                    alt="Foto de perfil"
                    className="perfil-avatar"
                />
                <h2 className="perfil-nombre">Nombre del Usuario</h2>
                <p className="perfil-rol">Rol o descripción breve</p>
            </div>
            <div className="perfil-info">
                <h3>Información personal</h3>
                <ul>
                    <li><strong>Email:</strong> usuario@email.com</li>
                    <li><strong>Teléfono:</strong> +52 123 456 7890</li>
                    <li><strong>Ubicación:</strong> Ciudad, País</li>
                </ul>
            </div>
            <div className="perfil-acciones">
                <button>Editar perfil</button>
                <button>Cerrar sesión</button>
            </div>
        </div>
    );
};

export default Perfill;