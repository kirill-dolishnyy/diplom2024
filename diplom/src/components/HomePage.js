import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import styles from './HomePage.module.css'; // Импорт CSS модулей
import { useNavigate } from 'react-router-dom'; // Добавьте этот импорт

function HomePage() {
  const [address, setAddress] = useState('');
  const navigate = useNavigate();
  const [rooms, setRooms] = useState(0); // Изначально установлено в 0 для "Студии"
  const [housingClass, setHousingClass] = useState('Эконом');
  const [area, setArea] = useState('');
  const [floor, setFloor] = useState('');

  const location = useLocation();

  const handleSubmit = (e) => {
    e.preventDefault();
    const data = {
      address,
      rooms,  // Теперь rooms уже в числовом формате
      housingClass,
      area: parseInt(area, 10), // Убедитесь, что area и floor также передаются как числа
      floor: parseInt(floor, 10)
    };
    console.log("Sending data:", data);  // Логирование данных перед отправкой

    fetch('http://127.0.0.1:8000/result/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        navigate('/result', { state: { result } }); // Используйте navigate вместо window.location.href
    })
    .catch(error => {
        console.error('Error:', error);
    });
  };

  return (
    <div className={styles.container}>
      <form onSubmit={handleSubmit} className={styles.formContainer}>
        <input
          type="text"
          className={styles.input}
          placeholder="Населенный пункт, улица, дом"
          value={address}
          onChange={(e) => setAddress(e.target.value)}
        />
        <div className={styles.buttonGroup}>
          {['Студия', '1', '2', '3', '4+'].map((room) => (
            <button
              type="button"
              key={room}
              className={room === (rooms === 0 ? 'Студия' : rooms.toString()) ? styles.activeButton : styles.button}
              onClick={() => setRooms(room === 'Студия' ? 0 : parseInt(room, 10))}
            >
              {room}
            </button>
          ))}
        </div>
        <div className={styles.buttonGroup}>
          {['бизнес', 'комфорт', 'эконом'].map((hClass) => (
            <button
              type="button"
              key={hClass}
              className={hClass === housingClass ? styles.activeButton : styles.button}
              onClick={() => setHousingClass(hClass)}
            >
              {hClass}
            </button>
          ))}
        </div>
        <input
          type="number"
          className={`${styles.input} ${styles.inputSmall}`}
          placeholder="Площадь"
          value={area}
          onChange={(e) => setArea(e.target.value)}
        />
        <input
          type="number"
          className={`${styles.input} ${styles.inputSmall}`}
          placeholder="Этаж"
          value={floor}
          onChange={(e) => setFloor(e.target.value)}
        />
        <button type="submit" className={styles.submitButton}>
          Предсказать цену
        </button>
      </form>
    </div>
  );
}

export default HomePage;