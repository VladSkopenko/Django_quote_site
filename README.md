### Кроки  для запуска застосунку:

1. **Запуск контейнера PostgreSQL:**
   Запустіть контейнер PostgreSQL з допомогою Docker:
   ```bash
   docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=1111 -d postgres
2. **Міграція:**
   Виконайте міграцію з допомогою django :
   ```bash
   py manage.py migrate 
3. **Міграція:**
   Наповніть базу даними за допомогою кастомного скрипта:
   ```bash
   py -m utils.migra
4. **Запуск сервера:**
    Запустіть застосунок:
    ```bash
   py manage.py runserver 
