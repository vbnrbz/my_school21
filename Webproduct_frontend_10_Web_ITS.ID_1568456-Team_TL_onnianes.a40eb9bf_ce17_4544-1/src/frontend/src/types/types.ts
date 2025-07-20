export interface Patient {
  id: string;
  name: string;
}

export interface PatientMetric {
  timestamp: string; // ISO-строка (в TS — string, даже если в Python datetime)
  pulse: number | null;
  resp_rate: number | null;
  bp: string | null;
  spo2: number | null;
  temperature: number | null;
}
