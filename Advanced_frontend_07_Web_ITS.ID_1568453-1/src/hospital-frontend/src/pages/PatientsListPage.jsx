import React, { useEffect, useState } from 'react';
import axios from 'axios';

const PatientsListPage = () => {
  const [patients, setPatients] = useState([]);
  const [editingId, setEditingId] = useState(null);
  const [editedPatient, setEditedPatient] = useState({});
  const [message, setMessage] = useState(null);
  const [error, setError] = useState(null);

  const fetchPatients = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/patients/all');
      setPatients(response.data);
    } catch (err) {
      console.error('Ошибка при загрузке пациентов:', err);
      setError('Не удалось загрузить пациентов.');
    }
  };

  useEffect(() => {
    fetchPatients();
  }, []);

  const handleEdit = (patient) => {
    setEditingId(patient.patient_id);
    setEditedPatient({
      fio: patient.fio,
      birth_date: patient.birth_date,
    });
    setMessage(null);
    setError(null);
  };

  const handleCancel = () => {
    setEditingId(null);
    setEditedPatient({});
  };

  const handleSave = async (id) => {
    try {
      await axios.patch(`http://localhost:8000/api/patients/${id}`, editedPatient);
      setMessage('Данные успешно обновлены.');
      setEditingId(null);
      fetchPatients();
    } catch (err) {
      console.error('Ошибка при обновлении:', err);
      setError('Ошибка при сохранении изменений.');
    }
  };

  return (
    <div className="container mt-4">
      <h2>Список пациентов</h2>

      {message && <div className="alert alert-success">{message}</div>}
      {error && <div className="alert alert-danger">{error}</div>}

      <table className="table mt-3">
        <thead>
          <tr>
            <th>UUID</th>
            <th>ФИО</th>
            <th>Дата рождения</th>
            <th>Возраст</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          {patients.map((patient) => (
            <tr key={patient.patient_id}>
              <td>{patient.patient_id}</td>
              <td>
                {editingId === patient.patient_id ? (
                  <input
                    type="text"
                    className="form-control"
                    value={editedPatient.fio}
                    onChange={(e) =>
                      setEditedPatient({ ...editedPatient, fio: e.target.value })
                    }
                  />
                ) : (
                  patient.fio
                )}
              </td>
              <td>
                {editingId === patient.patient_id ? (
                  <input
                    type="date"
                    className="form-control"
                    value={editedPatient.birth_date}
                    onChange={(e) =>
                      setEditedPatient({ ...editedPatient, birth_date: e.target.value })
                    }
                  />
                ) : (
                  patient.birth_date
                )}
              </td>
              <td>{patient.age}</td>
              <td>
                {editingId === patient.patient_id ? (
                  <>
                    <button
                      className="btn btn-success btn-sm me-2"
                      onClick={() => handleSave(patient.patient_id)}
                    >
                      Сохранить
                    </button>
                    <button className="btn btn-secondary btn-sm" onClick={handleCancel}>
                      Отмена
                    </button>
                  </>
                ) : (
                  <button
                    className="btn btn-warning btn-sm"
                    onClick={() => handleEdit(patient)}
                  >
                    Редактировать
                  </button>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default PatientsListPage;
