import React from 'react'
import Login from '../pages/Login'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; 
import Register from '../pages/Register'
import Inicio from '../pages/Inicio'
import Perfil from '../pages/Perfil'
import Opciones from '../pages/Opciones'
export default function Routing() {
  return (
    <div>


<Router>
        <Routes>

          <Route path="/" element={<Login/>}/>
          <Route path="/register" element={<Register/>}/>
          <Route path="/home" element={<Inicio/>}/>
          <Route path="/edit" element={<Perfil/>}/>
          <Route path="/contacto" element={<Opciones/>}/>
          
          
        </Routes>
      </Router> 


    </div>
  )
}
