FROM python:3.11-slim-bullseye
RUN apt update
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "hw/manage.py", "runserver", "0.0.0.0:8000"]