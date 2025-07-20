// src/components/CurrentMetrics.tsx
import React from 'react';
import { PatientMetric } from '../types/types';

interface CurrentMetricsProps {
  metrics: PatientMetric;  // один объект метрик
}

const THRESHOLDS = {
  HEART_RATE: { MIN: 60, MAX: 100, CRITICAL_MIN: 40, CRITICAL_MAX: 190 },
  SPO2: { MIN: 95, CRITICAL_MIN: 90 },
  TEMPERATURE: { MIN: 36, MAX: 37.5, CRITICAL_MIN: 35, CRITICAL_MAX: 39 },
  SYSTOLIC_PRESSURE: { MIN: 100, MAX: 140, CRITICAL_MIN: 90, CRITICAL_MAX: 180 },
  DIASTOLIC_PRESSURE: { MIN: 60, MAX: 90, CRITICAL_MIN: 50, CRITICAL_MAX: 120 },
};

type Zone = 'green' | 'yellow' | 'red';

function getZoneHeartRate(value: number | null): Zone {
  if (value === null) return 'green';
  if (value < THRESHOLDS.HEART_RATE.CRITICAL_MIN || value > THRESHOLDS.HEART_RATE.CRITICAL_MAX) return 'red';
  if (value < THRESHOLDS.HEART_RATE.MIN || value > THRESHOLDS.HEART_RATE.MAX) return 'yellow';
  return 'green';
}

function getZoneSpo2(value: number | null): Zone {
  if (value === null) return 'green';
  if (value < THRESHOLDS.SPO2.CRITICAL_MIN) return 'red';
  if (value < THRESHOLDS.SPO2.MIN) return 'yellow';
  return 'green';
}

function getZoneTemperature(value: number | null): Zone {
  if (value === null) return 'green';
  if (value < THRESHOLDS.TEMPERATURE.CRITICAL_MIN || value > THRESHOLDS.TEMPERATURE.CRITICAL_MAX) return 'red';
  if (value < THRESHOLDS.TEMPERATURE.MIN || value > THRESHOLDS.TEMPERATURE.MAX) return 'yellow';
  return 'green';
}

// Аналогично можно добавить зоны для давления, если нужно

const zoneColors: Record<Zone, string> = {
  green: '#4caf50',
  yellow: '#ffb300',
  red: '#f44336',
};

const CurrentMetrics: React.FC<CurrentMetricsProps> = ({ metrics }) => {
  const pulseZone = getZoneHeartRate(metrics.pulse);
  const spo2Zone = getZoneSpo2(metrics.spo2);
  const tempZone = getZoneTemperature(metrics.temperature);

  return (
    <div style={{ display: 'flex', gap: 20, flexWrap: 'wrap' }}>
      <MetricCard label="Пульс (уд/мин)" value={metrics.pulse} color={zoneColors[pulseZone]} />
      <MetricCard label="SpO2 (%)" value={metrics.spo2} color={zoneColors[spo2Zone]} />
      <MetricCard label="Температура (°C)" value={metrics.temperature} color={zoneColors[tempZone]} />
      {/* Можно добавить другие метрики по аналогии */}
    </div>
  );
};

interface MetricCardProps {
  label: string;
  value: number | null | undefined;
  color: string;
}

const MetricCard: React.FC<MetricCardProps> = ({ label, value, color }) => {
  return (
    <div
      style={{
        minWidth: 120,
        padding: 16,
        borderRadius: 8,
        backgroundColor: '#fff',
        boxShadow: `0 0 10px ${color}66`,
        border: `2px solid ${color}`,
        textAlign: 'center',
      }}
    >
      <div style={{ fontSize: 18, fontWeight: 'bold', color }}>{value !== null && value !== undefined ? value : '—'}</div>
      <div style={{ fontSize: 14, marginTop: 4 }}>{label}</div>
    </div>
  );
};

export default CurrentMetrics;
