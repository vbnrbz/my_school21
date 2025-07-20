// src/App.tsx
import React, { useEffect, useState, useCallback } from 'react';
import axios from 'axios';
import PatientCard from './components/PatientCard';
import { Patient, PatientMetric } from './types/types';

const API_BASE = 'http://localhost:8001';

const App: React.FC = () => {
  const [patients, setPatients] = useState<Patient[]>([]);
  const [selectedPatientId, setSelectedPatientId] = useState<string | null>(null);
  const [metrics, setMetrics] = useState<PatientMetric[]>([]);
  const [connectionIssue, setConnectionIssue] = useState(false);
  const [message, setMessage] = useState<string | null>(null);
  const [messageType, setMessageType] = useState<'error' | 'success'>('error');
  let successTimeout: number | null = null;

  // Получить список пациентов
  const fetchPatients = useCallback(async () => {
    try {
      const res = await axios.get<Patient[]>(`${API_BASE}/patients`);
      setPatients(res.data);
      setConnectionIssue(false);
      setMessage(null);
      setMessageType('success');
      if (res.data.length > 0 && !selectedPatientId) {
        setSelectedPatientId(res.data[0].id);
      }
    } catch (error) {
      setConnectionIssue(true);
      setMessage('Ошибка подключения при загрузке пациентов');
      setMessageType('error');
    }
  }, [selectedPatientId]);

  // Получить метрики выбранного пациента
  const fetchMetrics = useCallback(
    async (patientId: string) => {
      try {
        const res = await axios.get<PatientMetric[]>(`${API_BASE}/patient/${patientId}/metrics`);
        setMetrics(res.data);
        setConnectionIssue(false);
        setMessage('Данные успешно обновлены');
        setMessageType('success');

        if (successTimeout) clearTimeout(successTimeout);
        successTimeout = window.setTimeout(() => {
          setMessage(null);
        }, 2000);
      } catch (error) {
        setConnectionIssue(true);
        setMessage('Ошибка подключения при загрузке метрик');
        setMessageType('error');
      }
    },
    []
  );

  // Обработчик смены пациента
  const handlePatientChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const patientId = e.target.value;
    setSelectedPatientId(patientId);
    fetchMetrics(patientId);
  };

  // Закрыть сообщение об ошибке/успехе
  const handleCloseMessage = () => {
    setMessage(null);
  };

  // Инициализация: загрузить пациентов и метрики первого пациента
  useEffect(() => {
    fetchPatients();
  }, [fetchPatients]);

  // При смене selectedPatientId загружаем метрики
  useEffect(() => {
    if (selectedPatientId) {
      fetchMetrics(selectedPatientId);
    } else {
      setMetrics([]);
    }
  }, [selectedPatientId, fetchMetrics]);

  return (
    <div style={{ maxWidth: 1000, margin: '30px auto', fontFamily: 'Arial, sans-serif' }}>
      <h1>Мониторинг пациентов</h1>

      {message && (
        <div
          style={{
            padding: '10px 20px',
            marginBottom: 20,
            borderRadius: 5,
            color: '#fff',
            backgroundColor: messageType === 'error' ? '#f44336' : '#4caf50',
            cursor: 'pointer',
          }}
          onClick={handleCloseMessage}
          role="alert"
        >
          {message} (нажмите, чтобы закрыть)
        </div>
      )}

      <label htmlFor="patient-select" style={{ fontWeight: 'bold' }}>
        Выберите пациента:
      </label>
      <select
        id="patient-select"
        value={selectedPatientId || ''}
        onChange={handlePatientChange}
        style={{ marginLeft: 12, padding: 6, fontSize: 16 }}
      >
        {patients.map((patient) => (
          <option key={patient.id} value={patient.id}>
            {patient.name}
          </option>
        ))}
      </select>

      {selectedPatientId && metrics.length > 0 ? (
        <PatientCard patientName={patients.find(p => p.id === selectedPatientId)?.name || ''} metrics={metrics} />
      ) : (
        <p style={{ marginTop: 40 }}>Выберите пациента, чтобы увидеть метрики</p>
      )}
    </div>
  );
};

export default App;
