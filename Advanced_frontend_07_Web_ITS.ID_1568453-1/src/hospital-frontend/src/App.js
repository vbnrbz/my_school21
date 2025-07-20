import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import DoctorRegisterPage from './pages/DoctorRegisterPage';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import RoomList from './pages/RoomList';
import PatientRegisterPage from './pages/PatientRegisterPage';
import DoctorsListPage from './pages/DoctorsListPage';
import DoctorDetailsPage from './pages/DoctorDetailsPage';
import PatientsListPage from './pages/PatientsListPage';
import PatientLookupPage from './pages/PatientLookupPage';
import AppointmentCreatePage from './pages/AppointmentCreatePage';
import AppointmentCancelPage from './pages/AppointmentCancelPage';

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/rooms" element={<RoomList />} />
        <Route path="/register/doctor" element={<DoctorRegisterPage />} />
        <Route path="/register/patient" element={<PatientRegisterPage />} />
        <Route path="/doctors" element={<DoctorsListPage />} />
        <Route path="/doctor/:doctorId" element={<DoctorDetailsPage />} />
        <Route path="/patients" element={<PatientsListPage />} />
        <Route path="/patients/lookup" element={<PatientLookupPage />} />
        <Route path="/appointments/create" element={<AppointmentCreatePage />} />
        <Route path="/appointments/cancel" element={<AppointmentCancelPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
