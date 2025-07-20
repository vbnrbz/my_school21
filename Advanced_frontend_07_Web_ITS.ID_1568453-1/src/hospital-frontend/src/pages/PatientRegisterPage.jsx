import React, { useState } from 'react';

function PatientRegisterPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [fio, setFio] = useState('');
  const [birthDate, setBirthDate] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!username || !password || !fio || !birthDate) {
      setMessage('Пожалуйста, заполните все поля.');
      return;
    }

    const birth_date = birthDate ? new Date(birthDate).toISOString().split('T')[0] : null;

    try {
      const response = await fetch('http://localhost:8000/api/register/patient', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username,
          password,
          fio,
          birth_date,
        }),
      });

      if (response.ok) {
        setMessage('Регистрация успешна!');
        
        setUsername('');
        setPassword('');
        setFio('');
        setBirthDate('');
      } else {
        const errorData = await response.json();
        setMessage('Ошибка: ' + (errorData.message || 'Не удалось зарегистрироваться.'));
      }
    } catch (error) {
      setMessage('Ошибка сети: ' + error.message);
    }
  };

  return (
    <div>
      <h2>Регистрация пациента</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username: </label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Password: </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div>
          <label>ФИО: </label>
          <input
            type="text"
            value={fio}
            onChange={(e) => setFio(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Дата рождения: </label>
          <input
            type="date"
            value={birthDate}
            onChange={(e) => setBirthDate(e.target.value)}
            required
          />
        </div>
        <button type="submit">Зарегистрироваться</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default PatientRegisterPage;
