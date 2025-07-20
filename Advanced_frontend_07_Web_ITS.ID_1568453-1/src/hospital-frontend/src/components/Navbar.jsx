import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">Медицинская Система</Link>
        <div className="collapse navbar-collapse">
          <ul className="navbar-nav me-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/rooms">Кабинеты</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/doctors">Доктора</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/patients">Пациенты</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/register/doctor">Регистрация доктора</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/register/patient">Регистрация пациента</Link>
            </li>
            <li className="nav-item">
                <Link className="nav-link" to="/patients/lookup">Поиск пациента</Link>
            </li>
            <li className="nav-item">
                <Link className="nav-link" to="/appointments/create">Создать встречу</Link>
            </li>
            <li className="nav-item">
                <Link className="nav-link" to="/appointments/cancel">Отменить встречу</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
