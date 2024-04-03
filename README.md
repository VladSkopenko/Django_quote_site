Запуск Docker-контейнер, щоб створити сервер PostgreSQL:

docker run --name hw_project-postgres -p 5432:5432 -e POSTGRES_PASSWORD=987654321 -d postgres
Зв'язок з базою даних MongoDB:

quotes/utils.py
Mіграціюz бази даних із MongoDB у Postgres для сайту реалізована кастомним скриптом:

utils/migrations.py
командою з консолі:

py -m utils.migration
Запуск сервера командою:

py manage.py runserver
Посилання на сайт:

 http://127.0.0.1:8000/

This is a site with quotes, which has registration, profile and various functionality
