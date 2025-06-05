import React from 'react';

const Seguidoress = ({ seguidores = [] }) => {
    return (
        <div className="seguidores-container">
            <h2>Seguidores</h2>
            <ul className="seguidores-list">
                {seguidores.length === 0 ? (
                    <li>No tienes seguidores aún.</li>
                ) : (
                    seguidores.map((seguidor, idx) => (
                        <li key={idx} className="seguidor-item">
                            <img
                                src={seguidor.avatar || '/default-avatar.png'}
                                alt={seguidor.nombre}
                                className="seguidor-avatar"
                            />
                            <span className="seguidor-nombre">{seguidor.nombre}</span>
                        </li>
                    ))
                )}
            </ul>
        </div>
    );
};

export default Seguidoress;