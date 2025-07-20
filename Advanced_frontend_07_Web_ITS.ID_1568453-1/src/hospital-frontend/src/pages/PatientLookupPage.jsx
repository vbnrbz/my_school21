import React, { useState } from 'react';
import axios from 'axios';

const PatientLookupPage = () => {
  const [fio, setFio] = useState('');
  const [birthDate, setBirthDate] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSearch = async (e) => {
    e.preventDefault();
    setResult(null);
    setError(null);

    try {
      const response = await axios.get('http://localhost:8000/api/patients/lookup', {
        params: {
          fio,
          birth_date: birthDate,
        },
      });
      setResult(response.data.patient_id);
    } catch (err) {
      if (err.response && err.response.status === 404) {
        setError('Пациент не найден.');
      } else {
        setError('Произошла ошибка при поиске.');
      }
    }
  };

  return (
    <div className="container mt-4">
      <h2>Поиск UUID пациента</h2>

      <form onSubmit={handleSearch}>
        <div className="mb-3">
          <label className="form-label">ФИО пациента</label>
          <input
            type="text"
            className="form-control"
            value={fio}
            onChange={(e) => setFio(e.target.value)}
            required
          />
        </div>

        <div className="mb-3">
          <label className="form-label">Дата рождения</label>
          <input
            type="date"
            className="form-control"
            value={birthDate}
            onChange={(e) => setBirthDate(e.target.value)}
            required
          />
        </div>

        <button type="submit" className="btn btn-primary">Найти</button>
      </form>

      {result && (
        <div className="alert alert-success mt-3">
          UUID пациента: <strong>{result}</strong>
        </div>
      )}

      {error && (
        <div className="alert alert-danger mt-3">
          {error}
        </div>
      )}
    </div>
  );
};

export default PatientLookupPage;
