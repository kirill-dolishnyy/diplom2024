import './ResultPage.css';
import React from 'react';
import { useLocation } from 'react-router-dom';

function ResultPage() {
  const location = useLocation();
  const { result } = location.state || {}; // Добавлено значение по умолчанию {}

  return (
    <div className="result-container">
      <h1 className="result-header">Результат предсказания</h1>
      {result && <p className="result-price">Цена недвижимости: {result}</p>}
      {/* Отобразите здесь дополнительную информацию из ответа, если необходимо */}
    </div>
  );
}

export default ResultPage;