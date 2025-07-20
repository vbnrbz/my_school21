import React from 'react';
import { render, screen } from '@testing-library/react';
import DoctorList from '../components/DoctorList';

describe('DoctorList component', () => {
  it('отображает имя врача', () => {
    const mockDoctors = [
      { doctor_id: '123e4567-e89b-12d3-a456-426614174000', fio: 'Иван Иванов' },
    ];

    render(<DoctorList doctors={mockDoctors} />);

    expect(screen.getByText('Иван Иванов')).toBeInTheDocument();
  });
});
