import { Link } from 'react-router-dom';

export default function Navbarr() {
  return (
    <nav className="bg-black text-white shadow-lg p-4 flex items-center justify-between">
      <div className="text-xl font-bold tracking-wide">
        <Link to="/">Voz Ciudadana</Link>
      </div>

      <div className="space-x-4">
        <Link to="/" className="hover:text-yellow-400 transition">Inicio</Link>
        <Link to="/posts" className="hover:text-yellow-400 transition">Posts</Link>
        <Link to="/encuestas" className="hover:text-yellow-400 transition">Encuestas</Link>
        <Link to="/perfil" className="hover:text-yellow-400 transition">Perfil</Link>
      </div>
    </nav>
  );
}