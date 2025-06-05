import React, { useState, useEffect } from 'react';
import Publicacion from '../components/Publicacion/Publicacion';
import './Home.css';

const Inicioo = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
   
    const data = [
      {
        id: 1,
        usuario: 'jocksan_19',
        contenido: 'Primer día del proyecto, todo bien calidito ',
        comentarios: [
          { nombre: 'andrea_23', contenido: 'Mucho éxito, papi ' },
          { nombre: 'bryan_code', contenido: 'Pegala con todo' },
          { nombre: 'alex', contenido: '💪💪💪' }
        ]
      },
      {
        id: 2,
        usuario: 'jocksan_19',
        contenido: 'Me mojé todo saliendo del brete 😅',
        comentarios: [
          { nombre: 'luisito', contenido: 'Mae, fijo en Mora jaja' },
          { nombre: 'dani', contenido: 'Póngale abrigo, loco' }
        ]
      }
    ];

    setPosts(data);
  }, []);

  return (
    <div className="home-container">
      <h1 className="titulo-home">Inicio</h1>
      {posts.map(post => (
        <Publicacion key={post.id} post={post} />
      ))}
    </div>
  );
};

export default Inicioo;
