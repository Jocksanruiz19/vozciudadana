import React from 'react';
import styles from './Comentarios.module.css';

const Comentariosss = ({ nombre, contenido, fecha }) => {
  return (
    <div className={styles.comentario}>
      <div className={styles.header}>
        <div className={styles.avatar}>
          {nombre.charAt(0).toUpperCase()}
        </div>
        <div>
          <h4 className={styles.nombre}>{nombre}</h4>
          <p className={styles.fecha}>{fecha}</p>
        </div>
      </div>
      <p className={styles.contenido}>{contenido}</p>
    </div>
  );
};

const Comentarios = ({ listaComentarios }) => {
  return (
    <div className={styles.contenedor}>
      <h2 className={styles.titulo}>Comentarios</h2>
      {listaComentarios.map((coment, index) => (
        <Comentariosss
          key={index}
          nombre={coment.nombre}
          contenido={coment.contenido}
          fecha={coment.fecha}
        />
      ))}
    </div>
  );
};

export default Comentariosss