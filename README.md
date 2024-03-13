1.Запуск Docker-контейнер, щоб створити сервер PostgreSQL:
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres
2.Mіграціюz бази даних із MongoDB у Postgres для сайту реалізована кастомним скриптом:
utils/migrations.py
командою з консолі:
py -m utils.migration
3.Запуск сервера командою:
py manage.py runserver
4.Посилання на сайт:
http://127.0.0.1:8000/
