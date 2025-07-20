import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const DoctorsListPage = () => {
  const [doctors, setDoctors] = useState([]);
  const [editingId, setEditingId] = useState(null);
  const [editedDoctor, setEditedDoctor] = useState({});
  const navigate = useNavigate();

  useEffect(() => {
    fetchDoctors();
  }, []);

  const fetchDoctors = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/doctors/all');
      setDoctors(response.data);
    } catch (error) {
      console.error('Ошибка при загрузке списка докторов:', error);
    }
  };

  const handleEditClick = (doctor) => {
    setEditingId(doctor.doctor_id);
    setEditedDoctor({
      fio: doctor.fio,
      specialty: doctor.specialty,
      available: doctor.available,
    });
  };

  const handleSave = async (id) => {
    try {
      await axios.patch(`http://localhost:8000/api/doctors/${id}`, editedDoctor);
      setEditingId(null);
      fetchDoctors();
    } catch (error) {
      console.error('Ошибка при обновлении:', error);
    }
  };

  const handleCancel = () => {
    setEditingId(null);
    setEditedDoctor({});
  };

  return (
    <div className="container mt-4">
      <h2>Список докторов</h2>

      <table className="table">
        <thead>
          <tr>
            <th>UUID</th>
            <th>ФИО</th>
            <th>Специальность</th>
            <th>Доступен</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          {doctors.map((doctor) => (
            <tr key={doctor.doctor_id}>
              <td>{doctor.doctor_id}</td>

              <td>
                {editingId === doctor.doctor_id ? (
                  <input
                    type="text"
                    value={editedDoctor.fio}
                    onChange={(e) =>
                      setEditedDoctor({ ...editedDoctor, fio: e.target.value })
                    }
                    className="form-control"
                  />
                ) : (
                  doctor.fio
                )}
              </td>

              <td>
                {editingId === doctor.doctor_id ? (
                  <input
                    type="text"
                    value={editedDoctor.specialty}
                    onChange={(e) =>
                      setEditedDoctor({ ...editedDoctor, specialty: e.target.value })
                    }
                    className="form-control"
                  />
                ) : (
                  doctor.specialty
                )}
              </td>

              <td>
                {editingId === doctor.doctor_id ? (
                  <input
                    type="checkbox"
                    checked={editedDoctor.available}
                    onChange={(e) =>
                      setEditedDoctor({ ...editedDoctor, available: e.target.checked })
                    }
                  />
                ) : doctor.available ? (
                  'Да'
                ) : (
                  'Нет'
                )}
              </td>

              <td>
                {editingId === doctor.doctor_id ? (
                  <>
                    <button
                      className="btn btn-success btn-sm me-2"
                      onClick={() => handleSave(doctor.doctor_id)}
                    >
                      Сохранить
                    </button>
                    <button
                      className="btn btn-secondary btn-sm"
                      onClick={handleCancel}
                    >
                      Отмена
                    </button>
                  </>
                ) : (
                  <>
                    <button
                      className="btn btn-warning btn-sm me-2"
                      onClick={() => handleEditClick(doctor)}
                    >
                      Редактировать
                    </button>
                    <button
                      className="btn btn-info btn-sm"
                      onClick={() => navigate(`/doctor/${doctor.doctor_id}`)}
                    >
                      Подробнее
                    </button>
                  </>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DoctorsListPage;
