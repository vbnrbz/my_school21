import React, { useEffect, useState } from 'react';
import axios from 'axios';
import RoomForm from '../components/RoomForm';

function RoomList() {
  const [rooms, setRooms] = useState([]);
  const [error, setError] = useState(null);
  const [editingRoomId, setEditingRoomId] = useState(null);
  const [editedRoom, setEditedRoom] = useState({});

  const fetchRooms = () => {
    axios.get('http://localhost:8000/api/room')
      .then(response => setRooms(response.data))
      .catch(err => {
        console.error('Ошибка при загрузке кабинетов:', err);
        setError('Не удалось загрузить кабинеты');
      });
  };

  useEffect(() => {
    fetchRooms();
  }, []);

  const handleEditClick = (room) => {
    setEditingRoomId(room.room_id);
    setEditedRoom({ room_name: room.room_name, available: room.available });
  };

  const handleSaveEdit = async (id) => {
    try {
      await axios.patch(`http://localhost:8000/api/room/${id}`, editedRoom);
      setEditingRoomId(null);
      setEditedRoom({});
      fetchRooms();
    } catch (err) {
      console.error('Ошибка при редактировании:', err);
    }
  };

  const handleDelete = async (id) => {
    const confirm = window.confirm('Вы уверены, что хотите удалить кабинет?');
    if (!confirm) return;

    try {
      await axios.delete(`http://localhost:8000/api/room/${id}`);
      fetchRooms();
    } catch (err) {
      console.error('Ошибка при удалении:', err);
    }
  };

  return (
    <div className="container mt-4">
      <h2>Список кабинетов</h2>

      <RoomForm onRoomCreated={fetchRooms} />

      {error && <div className="alert alert-danger">{error}</div>}

      <table className="table mt-3">
        <thead>
          <tr>
            <th>ID</th>
            <th>Название</th>
            <th>Доступен</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          {rooms.map((room) => (
            <tr key={room.room_id}>
              <td>{room.room_id}</td>

              <td>
                {editingRoomId === room.room_id ? (
                  <input
                    type="text"
                    className="form-control"
                    value={editedRoom.room_name}
                    onChange={(e) => setEditedRoom({ ...editedRoom, room_name: e.target.value })}
                  />
                ) : (
                  room.room_name
                )}
              </td>

              <td>
                {editingRoomId === room.room_id ? (
                  <input
                    type="checkbox"
                    checked={editedRoom.available}
                    onChange={(e) => setEditedRoom({ ...editedRoom, available: e.target.checked })}
                  />
                ) : (
                  room.available ? 'Да' : 'Нет'
                )}
              </td>

              <td>
                {editingRoomId === room.room_id ? (
                  <>
                    <button
                      className="btn btn-success btn-sm me-2"
                      onClick={() => handleSaveEdit(room.room_id)}
                    >
                      Сохранить
                    </button>
                    <button
                      className="btn btn-secondary btn-sm"
                      onClick={() => setEditingRoomId(null)}
                    >
                      Отмена
                    </button>
                  </>
                ) : (
                  <>
                    <button
                      className="btn btn-warning btn-sm me-2"
                      onClick={() => handleEditClick(room)}
                    >
                      Редактировать
                    </button>
                    <button
                      className="btn btn-danger btn-sm"
                      onClick={() => handleDelete(room.room_id)}
                    >
                      Удалить
                    </button>
                  </>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default RoomList;
