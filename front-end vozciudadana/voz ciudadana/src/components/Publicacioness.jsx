import React from 'react';
import './Publicacion.css';
import { useNavigate } from 'react-router-dom';

const Publicacioness = ({ post }) => {
  const navigate = useNavigate();

  const handleVerComentarios = () => {
    navigate(`/post/${post.id}`);
  };

  return (
    <div className="card-post">
      <div className="post-header">
        <div className="avatar">{post.usuario.charAt(0).toUpperCase()}</div>
        <span className="usuario">@{post.usuario}</span>
      </div>

      <p className="contenido">{post.contenido}</p>

      <div className="comentarios-preview">
        {post.comentarios.slice(0, 2).map((comentario, idx) => (
          <p key={idx} className="comentario">
            <strong>{comentario.nombre}:</strong> {comentario.contenido}
          </p>
        ))}
        {post.comentarios.length > 2 && (
          <button className="btn-ver-comentarios" onClick={handleVerComentarios}>
            Ver todos los comentarios ({post.comentarios.length})
          </button>
        )}
      </div>
    </div>
  );
};

export default Publicacioness;