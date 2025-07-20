import React, { useState } from 'react';
import axios from 'axios';

const AppointmentCancelPage = () => {
  const [appointmentId, setAppointmentId] = useState('');
  const [message, setMessage] = useState('');

  const handleCancel = async (e) => {
    e.preventDefault();
    setMessage('');

    try {
      const response = await axios.post('http://localhost:8000/api/appointments/cancel', {
        appointment_id: appointmentId,
      });

      if (response.status === 200) {
        setMessage('Встреча успешно отменена.');
      } else {
        setMessage('Не удалось отменить встречу.');
      }
    } catch (error) {
      if (error.response && error.response.status === 404) {
        setMessage('Встреча с таким ID не найдена.');
      } else {
        setMessage('Произошла ошибка при отмене встречи.');
        console.error(error);
      }
    }
  };

  return (
    <div>
      <h2>Отмена встречи</h2>
      <form onSubmit={handleCancel}>
        <label>UUID встречи:</label>
        <input
          type="text"
          value={appointmentId}
          onChange={(e) => setAppointmentId(e.target.value)}
          placeholder="Введите UUID встречи"
          required
        />
        <button type="submit">Отменить встречу</button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
};

export default AppointmentCancelPage;
