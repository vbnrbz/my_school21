import React, { useEffect, useState } from 'react';
import axios from 'axios';

const AppointmentCreatePage = () => {
  const [formData, setFormData] = useState({
    doctor: '',
    patient: '',
    room: '',
    date: '',
    notes: '',
    prescriptions: {},
    cancelled: false,
  });

  const [doctors, setDoctors] = useState([]);
  const [patients, setPatients] = useState([]);
  const [rooms, setRooms] = useState([]);
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/api/doctors/all')
      .then(res => setDoctors(res.data))
      .catch(err => console.error('Ошибка загрузки врачей:', err));

    axios.get('http://localhost:8000/api/patients/all')
      .then(res => setPatients(res.data))
      .catch(err => console.error('Ошибка загрузки пациентов:', err));

    axios.get('http://localhost:8000/api/room')
      .then(res => setRooms(res.data))
      .catch(err => console.error('Ошибка загрузки кабинетов:', err));
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value,
    }));
  };

  const setNextDayMorning = () => {
    const now = new Date();
    const nextDay = new Date(now);
    nextDay.setDate(now.getDate() + 1);
    nextDay.setHours(9, 5, 0, 0);

    const tzOffset = nextDay.getTimezoneOffset() * 60000;
    const localISOTime = new Date(nextDay - tzOffset).toISOString().slice(0, 16);

    setFormData(prev => ({
      ...prev,
      date: localISOTime,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      ...formData,
      prescriptions: {},
    };

    try {
      await axios.post('http://localhost:8000/api/appointments/create', payload);
      setMessage('Встреча успешно создана!');
      setFormData({
        doctor: '',
        patient: '',
        room: '',
        date: '',
        notes: '',
        prescriptions: {},
        cancelled: false,
      });
    } catch (error) {
      console.error('Ошибка создания встречи:', error);
      setMessage('Ошибка при создании встречи.');
    }
  };

  return (
    <div>
      <h2>Создание встречи</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Врач:</label>
          <select name="doctor" value={formData.doctor} onChange={handleChange} required>
            <option value="">Выберите врача</option>
            {doctors.map(doc => (
              <option key={doc.doctor_id} value={doc.doctor_id}>{doc.fio}</option>
            ))}
          </select>
        </div>

        <div>
          <label>Пациент:</label>
          <select name="patient" value={formData.patient} onChange={handleChange} required>
            <option value="">Выберите пациента</option>
            {patients.map(pat => (
              <option key={pat.patient_id} value={pat.patient_id}>{pat.fio}</option>
            ))}
          </select>
        </div>

        <div>
          <label>Кабинет:</label>
          <select name="room" value={formData.room} onChange={handleChange} required>
            <option value="">Выберите кабинет</option>
            {rooms.map(room => (
              <option key={room.room_id} value={room.room_id}>{room.room_name}</option>
            ))}
          </select>
        </div>

        <div>
          <label>Дата и время встречи:</label>
          <input
            type="datetime-local"
            name="date"
            value={formData.date}
            onChange={handleChange}
            required
          />
          <button type="button" onClick={setNextDayMorning}>
            Установить на 9:05 утра следующего дня
          </button>
        </div>

        <div>
          <label>Заметки:</label>
          <textarea name="notes" value={formData.notes} onChange={handleChange} />
        </div>

        <button type="submit">Создать встречу</button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
};

export default AppointmentCreatePage;
