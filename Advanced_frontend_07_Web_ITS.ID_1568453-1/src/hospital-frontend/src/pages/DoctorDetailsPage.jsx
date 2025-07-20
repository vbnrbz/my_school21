import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const DoctorDetailsPage = () => {
  const { doctorId } = useParams();
  const [doctor, setDoctor] = useState(null);
  const [appointments, setAppointments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [appointmentsLoading, setAppointmentsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchDoctor = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/doctors/${doctorId}`);
        setDoctor(response.data);
      } catch (err) {
        console.error('Ошибка при загрузке данных врача:', err);
        setError('Не удалось загрузить данные врача.');
      } finally {
        setLoading(false);
      }
    };

    const fetchAppointments = async () => {
      setAppointmentsLoading(true);
      try {
        const response = await axios.get(`http://localhost:8000/api/doctors/${doctorId}/appointments`);
        setAppointments(response.data);
      } catch (err) {
        console.error('Ошибка при загрузке встреч:', err);
        setError('Не удалось загрузить встречи врача.');
      } finally {
        setAppointmentsLoading(false);
      }
    };

    fetchDoctor();
    fetchAppointments();
  }, [doctorId]);

  const handleCancelAppointment = async (appointmentId) => {
    try {
      await axios.post('http://localhost:8000/api/appointments/cancel', {
        appointment_id: appointmentId,
      });
      setMessage('Встреча успешно отменена');

      const response = await axios.get(`http://localhost:8000/api/doctors/${doctorId}/appointments`);
      setAppointments(response.data);
    } catch (err) {
      console.error('Ошибка при отмене встречи:', err);
      setMessage('Не удалось отменить встречу.');
    }
  };

  if (loading) return <p className="m-4">Загрузка...</p>;
  if (error) return <p className="m-4 text-danger">{error}</p>;
  if (!doctor) return <p className="m-4">Доктор не найден.</p>;

  return (
    <div className="container mt-4">
      <h2>Детали врача</h2>

      <table className="table mt-3">
        <tbody>
          <tr>
            <th scope="row">UUID</th>
            <td>{doctor.doctor_id}</td>
          </tr>
          <tr>
            <th scope="row">ФИО</th>
            <td>{doctor.fio}</td>
          </tr>
          <tr>
            <th scope="row">Специальность</th>
            <td>{doctor.specialty}</td>
          </tr>
          <tr>
            <th scope="row">Доступность</th>
            <td>{doctor.available ? 'Да' : 'Нет'}</td>
          </tr>
        </tbody>
      </table>

      <h4 className="mt-5">Встречи врача</h4>
      {appointmentsLoading ? (
        <p>Загрузка встреч...</p>
      ) : appointments.length === 0 ? (
        <p>Нет назначенных встреч.</p>
      ) : (
        <table className="table mt-3">
          <thead>
            <tr>
              <th>Дата</th>
              <th>Пациент</th>
              <th>Кабинет</th>
              <th>Статус</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {appointments.map((appt) => (
              <tr key={appt.appointment_id}>
                <td>{new Date(appt.date).toLocaleString()}</td>
                <td>{appt.patient}</td>
                <td>{appt.room}</td>
                <td>{appt.cancelled ? 'Отменена' : 'Активна'}</td>
                <td>
                  {!appt.cancelled && (
                    <button
                      className="btn btn-sm btn-danger"
                      onClick={() => handleCancelAppointment(appt.appointment_id)}
                    >
                      Отменить
                    </button>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {message && <p className="mt-3">{message}</p>}
    </div>
  );
};

export default DoctorDetailsPage;
