import React, { useState } from 'react';
import axios from 'axios';

const DoctorRegisterForm = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    fio: '',
    specialty: '',
  });

  const [message, setMessage] = useState(null);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage(null);
    setError(null);

    // валидация
    const { username, password, fio, specialty } = formData;
    if (!username || !password || !fio || !specialty) {
      setError('Все поля обязательны');
      return;
    }

    try {
      await axios.post('http://localhost:8000/api/register/doctor', formData);
      setMessage('Доктор успешно зарегистрирован');
      setFormData({ username: '', password: '', fio: '', specialty: '' });
    } catch (err) {
      console.error('Ошибка при регистрации:', err);
      setError('Ошибка при регистрации. Проверьте корректность данных.');
    }
  };

  return (
    <div className="container mt-4">
      <h2>Регистрация доктора</h2>
      {message && <div className="alert alert-success">{message}</div>}
      {error && <div className="alert alert-danger">{error}</div>}

      <form onSubmit={handleSubmit} className="mt-3">
        <div className="form-group">
          <label>Логин</label>
          <input
            type="text"
            name="username"
            className="form-control"
            value={formData.username}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group mt-2">
          <label>Пароль</label>
          <input
            type="password"
            name="password"
            className="form-control"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group mt-2">
          <label>ФИО</label>
          <input
            type="text"
            name="fio"
            className="form-control"
            value={formData.fio}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group mt-2">
          <label>Специальность</label>
          <input
            type="text"
            name="specialty"
            className="form-control"
            value={formData.specialty}
            onChange={handleChange}
            required
          />
        </div>

        <button type="submit" className="btn btn-primary mt-3">
          Зарегистрировать
        </button>
      </form>
    </div>
  );
};

export default DoctorRegisterForm;
