import React, { useEffect, useState } from 'react'
import { Link/* , useNavigate  */} from 'react-router-dom';
import UserLogin from '../services/UserLogin';

function Register() {
    

  const [Username,SetNombreUsuario]=useState()
  const [EmailUser,SetEmailUsuario]=useState()
  const [PasswordUsuario, SetPasswordUsuario]=useState()

  function nombre(evento) {
    SetNombreUsuario(evento.target.value)
  }

  function email(evento) {
    SetEmailUsuario(evento.target.value)
  }

  function password(evento) {
    SetPasswordUsuario(evento.target.value)
  }

  function cargar() {
   UserLogin.postUsers(Username,EmailUser,PasswordUsuario)

    
    
  }



  return (
    <div>
    <h1>Crear cuenta</h1>

     
   <label htmlFor="">Username</label>
   <input value={Username} onChange={nombre} type='text' />
   <br />


   <label htmlFor="">Email</label>
   <input value={EmailUser} onChange={email} type='text' />
   <br />


   <label htmlFor="">Password</label>
   <input value={PasswordUsuario} onChange={password} type='text' />
   <br />
   <button onClick={cargar}>Registrarse</button>
   <p>Ya tienes una cuenta? <Link to= "/">Inicia aqui</Link></p>
 </div>
  )
}

export default RegisterUser