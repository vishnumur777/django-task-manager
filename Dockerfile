FROM python:3.11

WORKDIR app/

COPY . app/

RUN ls

EXPOSE 8000

RUN python3 manage.py runserver