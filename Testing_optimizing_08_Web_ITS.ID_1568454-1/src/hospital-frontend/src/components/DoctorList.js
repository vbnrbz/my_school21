import React from 'react';

const DoctorList = ({ doctors }) => (
  <ul>
    {doctors.map((doc) => (
      <li key={doc.doctor_id}>{doc.fio}</li>
    ))}
  </ul>
);

export default DoctorList;
