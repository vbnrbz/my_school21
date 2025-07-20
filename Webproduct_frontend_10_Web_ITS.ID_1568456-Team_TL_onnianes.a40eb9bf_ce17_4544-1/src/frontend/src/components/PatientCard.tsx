// src/components/PatientCard.tsx
import React from 'react';
import CurrentMetrics from './CurrentMetrics';
import PatientMetricsChart from './PatientMetricsChart';
import { PatientMetric } from '../types/types';

interface PatientCardProps {
  patientName: string;
  metrics: PatientMetric[];
}

const PatientCard: React.FC<PatientCardProps> = ({ patientName, metrics }) => {
  const currentMetrics = metrics.length > 0 ? metrics[metrics.length - 1] : null;

  return (
    <div
      style={{
        border: '1px solid #ddd',
        borderRadius: 8,
        padding: 16,
        maxWidth: 900,
        margin: '20px auto',
        backgroundColor: '#fafafa',
        boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
      }}
    >
      <h2 style={{ marginBottom: 16 }}>{patientName}</h2>

      {currentMetrics ? (
        <CurrentMetrics metrics={currentMetrics} />
      ) : (
        <p>Нет текущих данных метрик</p>
      )}

      <div style={{ marginTop: 40 }}>
        <PatientMetricsChart metrics={metrics} />
      </div>
    </div>
  );
};

export default PatientCard;
