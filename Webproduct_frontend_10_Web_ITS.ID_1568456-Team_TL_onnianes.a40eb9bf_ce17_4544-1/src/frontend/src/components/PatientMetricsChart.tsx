import React, { useMemo } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  TimeScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  ChartOptions,
  ChartData,
} from 'chart.js';
import 'chartjs-adapter-date-fns';
import zoomPlugin from 'chartjs-plugin-zoom';
import { Line } from 'react-chartjs-2';
import { PatientMetric } from '../types/types';

ChartJS.register(
  CategoryScale,
  LinearScale,
  TimeScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  zoomPlugin
);

interface PatientMetricsChartProps {
  metrics: PatientMetric[];
}

const CHART_HEIGHT = 250;

const PatientMetricsChart: React.FC<PatientMetricsChartProps> = ({ metrics }) => {
  // useMemo вызываем всегда
  const chartsConfig = useMemo(() => {
    const keys = [
      { key: 'pulse', label: 'Пульс', color: 'rgba(75,192,192,1)' },
      { key: 'resp_rate', label: 'Частота дыхания', color: 'rgba(255,99,132,1)' },
      { key: 'spo2', label: 'SpO2', color: 'rgba(54,162,235,1)' },
      { key: 'temperature', label: 'Температура', color: 'rgba(255,206,86,1)' },
    ] as const;

    return keys.map(({ key, label, color }) => {
      const data = metrics.map(m =>
        m[key] !== null && m[key] !== undefined ? Number(m[key]) : null
      );

      const chartData: ChartData<'line'> = {
        labels: metrics.map(m => new Date(m.timestamp)),
        datasets: [
          {
            label,
            data,
            borderColor: color,
            backgroundColor: color.replace('1)', '0.2)'),
            spanGaps: true,
            tension: 0.2,
            fill: false,
          },
        ],
      };

      const chartOptions: ChartOptions<'line'> = {
        responsive: true,
        maintainAspectRatio: false,
        interaction: {
          mode: 'nearest',
          intersect: false,
        },
        scales: {
          x: {
            type: 'time',
            time: {
              unit: 'minute',
              tooltipFormat: 'dd.MM.yyyy HH:mm',
            },
            title: {
              display: true,
              text: 'Время',
            },
          },
          y: {
            beginAtZero: false,
            title: {
              display: true,
              text: label,
            },
          },
        },
        plugins: {
          zoom: {
            zoom: {
              wheel: { enabled: true },
              pinch: { enabled: true },
              mode: 'x',
            },
            pan: {
              enabled: true,
              mode: 'x',
            },
          },
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: label,
          },
        },
      };

      return { chartData, chartOptions, key };
    });
  }, [metrics]);

  if (metrics.length === 0) {
    return <p>Нет данных для отображения графиков</p>;
  }

  return (
    <div>
      {chartsConfig.map(({ chartData, chartOptions, key }) => (
        <div
          key={key}
          style={{
            height: CHART_HEIGHT,
            width: '100%',
            marginTop: 20,
          }}
        >
          <Line data={chartData} options={chartOptions} />
        </div>
      ))}
    </div>
  );
};

export default PatientMetricsChart;
