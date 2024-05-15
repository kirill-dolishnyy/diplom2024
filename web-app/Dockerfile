# Используйте базовый образ Node.js
FROM node:14

# Установите рабочую директорию в контейнере
WORKDIR /app

# Скопируйте файлы зависимостей
COPY package.json package-lock.json ./

# Установите зависимости
RUN npm install

# Скопируйте остальные файлы проекта
COPY . .

# Соберите статические файлы
RUN npm run build

# Установите serve для запуска собранного проекта
RUN npm install -g serve

# Укажите порт
EXPOSE 3000

# Запустите приложение
CMD ["serve", "-s", "build", "-l", "3000"]