import React, { useState } from 'react';
import axios from 'axios';

const RoomForm = ({ onRoomCreated }) => {
  const [roomName, setRoomName] = useState('');
  const [available, setAvailable] = useState(true);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/room/create', {
        room_name: roomName.trim(),
        available: available,
      });
      console.log('Кабинет создан:', response.data);
      setRoomName('');
      setAvailable(true);
      if (onRoomCreated) onRoomCreated();
    } catch (error) {
      console.error('Ошибка при создании кабинета: ', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-3">
      <div className="form-group">
        <label>Название кабинета</label>
        <input
          type="text"
          className="form-control"
          value={roomName}
          onChange={(e) => setRoomName(e.target.value)}
          required
        />
      </div>
      <div className="form-group form-check mt-2">
        <input
          type="checkbox"
          className="form-check-input"
          id="availableCheck"
          checked={available}
          onChange={(e) => setAvailable(e.target.checked)}
        />
        <label className="form-check-label" htmlFor="availableCheck">
          Кабинет доступен
        </label>
      </div>
      <button type="submit" className="btn btn-primary mt-3">
        Создать кабинет
      </button>
    </form>
  );
};

export default RoomForm;