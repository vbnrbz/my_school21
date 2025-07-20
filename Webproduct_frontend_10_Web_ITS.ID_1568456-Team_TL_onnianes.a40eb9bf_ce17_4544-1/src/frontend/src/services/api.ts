import axios from 'axios';
import { Patient, PatientMetric } from '../types/types';

const api = axios.create({
  baseURL: 'http://localhost:8001', // или другой адрес, если фронт и бэк на разных портах
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Получить всех пациентов
export const getPatients = async (): Promise<Patient[]> => {
  const response = await api.get<Patient[]>('/patients');
  return response.data;
};

// Получить метрики конкретного пациента
export const getPatientMetrics = async (patientId: string): Promise<PatientMetric[]> => {
  const response = await api.get<PatientMetric[]>(`/patient/${patientId}/metrics`);
  return response.data;
};
