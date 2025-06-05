import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';

import UserLogin from '../services/UserLogin';

function Loginn() {
    const [nombreUsuario, setNombreUsuario] = useState('');
    const [passwordUsuario, setPasswordUsuario] = useState('');
    const [usuarios, setUsuarios] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        async function fetchDataUsers() {
            const datos = await UserLogin.getUsers();
            setUsuarios(datos);
        }
        fetchDataUsers();
    }, []);

    function handleNombreChange(event) {
        setNombreUsuario(event.target.value);
    }

    function handlePasswordChange(event) {
        setPasswordUsuario(event.target.value);
    }

    function validar() {
        const usuarioValido = usuarios.find(
            (usuario) =>
                usuario.nombre === nombreUsuario && usuario.password === passwordUsuario
        );

        if (usuarioValido) {
            localStorage.setItem("llave", "usuario registrado");
            navigate('/home');
        } else {
            alert('Nombre de usuario o contraseña incorrectos');
        }
    }

    return (
        <div>
            <label htmlFor="nombre">Nombre</label>
            <input
                id="nombre"
                name="nombre"
                value={nombreUsuario}
                onChange={handleNombreChange}
                type="text"
            />
            <label htmlFor="password">Contraseña</label>
            <input
                id="password"
                name="password"
                value={passwordUsuario}
                onChange={handlePasswordChange}
                type="password"
            />
            <button onClick={validar}>Iniciar</button>
            <p>
                ¿No tienes una cuenta? <Link to="/register">Registrarme</Link>
            </p>
        </div>
    );
}

export default Loginn;
