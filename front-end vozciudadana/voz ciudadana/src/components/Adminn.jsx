import React from 'react';
import './Admin.css';

const Adminn = ({ tipo, cantidad, color }) => {
  return (
    <div className="card-admin" style={{ borderLeft: `6px solid ${color}` }}>
      <p className="admin-tipo">{tipo}</p>
      <h2 className="admin-cantidad">{cantidad}</h2>
    </div>
  );
};

export default Adminn;